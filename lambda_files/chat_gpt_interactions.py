import openai
import tiktoken
from dynamo_db_interactions import update_user_message
from dynamo_db_interactions import update_assistant_message

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def chat_gpt_message(messages: list, prompt: str, userID: str, table: None):
    input = {"role": "user", "content": prompt}
    update_user_message(userID=userID, input=input, table=table)
    message_history = messages
    message_history.append(input)
    max_tokens = 2000
    max_token_length = 14000
    remaining_tokens = max_token_length - num_tokens_from_string(string=(input["content"]), encoding_name="gpt2")
    total_token_length = 0  # Variable to track the total token length

    for i in range(len(message_history) - 1, -1, -1):
      message = message_history[i]
      tokens = num_tokens_from_string(string=message["content"], encoding_name="gpt2")
      if total_token_length + remaining_tokens <= max_token_length:
        remaining_tokens -= tokens
        total_token_length += tokens
        print(total_token_length)
      else:
        message_history = message_history[i + 1 :]
        break
    
    print(remaining_tokens)
    print(message_history)
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=message_history,
            max_tokens=max_tokens,
        )
        update_assistant_message(
            userID=userID, response=completion["choices"][0]["message"], table=table
        )
        chat_gpt_response = completion["choices"][0]["message"]["content"]
        return chat_gpt_response
    except openai.error.InvalidRequestError as e:
        print(e)
        response = "The prompt was too long for me to process. Think of a shorter prompt and try again."
        return response
    except openai.error.APIError as e:
        print(e)
        response = "The OpenAI servers are overloaded right now. Retry your prompt"
        return response
