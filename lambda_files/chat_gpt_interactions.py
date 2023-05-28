import openai
from dynamo_db_interactions import update_user_message
from dynamo_db_interactions import update_assistant_message


def chat_gpt_message(messages, prompt, userID, table):
    input = {"role": "user", "content": prompt}
    update_user_message(userID=userID, input=input,table=table)
    message_history = list(messages)
    message_history.append(input)
    
    max_tokens = 3000
    remaining_tokens = max_tokens - len(input["content"])
    for i in range(len(message_history) - 1, -1, -1):
        message = message_history[i]
        tokens = len(message["content"])
        if tokens <= remaining_tokens:
            remaining_tokens -= tokens
        else:
            message_history = message_history[i + 1 :]
            break
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history,
        max_tokens=max_tokens,
    )
    update_assistant_message(userID=userID,response=completion["choices"][0]["message"], table=table)
    chat_gpt_response = completion["choices"][0]["message"]["content"]
    return chat_gpt_response