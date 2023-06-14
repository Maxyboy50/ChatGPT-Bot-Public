import openai
from dynamo_db_interactions import update_user_message
from dynamo_db_interactions import update_assistant_message


def chat_gpt_message(messages: list, prompt: str, userID: str, table: None):
    input = {"role": "user", "content": prompt}
    update_user_message(userID=userID, input=input, table=table)
    message_history = messages
    message_history.append(input)
    max_tokens = 16000
    remaining_tokens = max_tokens - len(input["content"])
    for i in range(len(message_history) - 1, -1, -1):
        message = message_history[i]
        tokens = len(message["content"])
        if tokens <= remaining_tokens:
            remaining_tokens -= tokens
        else:
            message_history = message_history[i + 1 :]
            break
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
    except openai.error.InvalidRequestError:
        response = "The prompt was too long for me to process. Think of a shorter prompt and try again."
        return response
    except openai.error.APIError:
        response = "The OpenAI servers are overloaded right now. Retry your prompt"
        return response
