import requests
import openai
import time
import os
from dynamo_db_interactions import fetch_message_history
from chat_gpt_interactions import chat_gpt_message


API_KEY = os.getenv('API_KEY')
openai.api_key = API_KEY

def defer(interaction_id: str, interaction_token: str):
        url = f'https://discord.com/api/v10/interactions/{interaction_id}/{interaction_token}/callback'
        response = {'type': 5}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, headers=headers,json=response)
    
def follow_up(response: str, application_id: str, interaction_token: str):
        url = f'https://discord.com/api/v10/webhooks/{application_id}/{interaction_token}'
        headers = {"Content-Type": "application/json"}
        response = {"content": f'{response}'}
        r = requests.post(url, json=response)
        if "BASE_TYPE_MAX_LENGTH" in r.text:
          too_long_payload = {"content": "The prompt/reponse was too long to be returned to Discord. Think of a shorter prompt and try again."}
          r = requests.post(url,headers=headers,json=too_long_payload)
          
def command_handler(command_name: str, interaction_token: str, userID: str, interaction_id: str, dynamo_db_table: None, application_id: str, command_value: str):
      try:
        defer(interaction_id=interaction_id,interaction_token=interaction_token)
        time.sleep(.5)
        if command_name == "chatgptprompt":
          conversation_history = fetch_message_history(userID=userID,table=dynamo_db_table)
          assistant_reponse = chat_gpt_message(messages=conversation_history,prompt=command_value,userID=userID, table=dynamo_db_table)
          follow_up(response=assistant_reponse, application_id=application_id, interaction_token=interaction_token)
        else:
          follow_up(response="Sorry, that is an invalid command/option", application_id=application_id, interaction_token=interaction_token)
      except openai.error.RateLimitError:
        follow_up(response="Sorry, the OpenAI servers are overloaded right now, please try again shortly", application_id=application_id, interaction_token=interaction_token)