- [Serverless ChatGPT Bot](#serverless-chatgpt-bot)
  - [Overview:](#overview)
    - [Technologies used:](#technologies-used)
      - [Prompt:](#prompt)
      - [Bot thinking:](#bot-thinking)
      - [Response:](#response)
      - [Reference to message history:](#reference-to-message-history)
# Serverless ChatGPT Bot

## Overview:
This purpose of this project was to integrate the incredibly powerful OpenAI API with the popular community platform Discord to provide ChatGPT-like functionality from within the platform. The bot can respond to any prompt and has 

### Technologies used:
The code for this bot is written entirely in Python and leverages AWS API Gateway, AWS Lambda, and AWS DynamoDB for receiving, processing, and storing events received from Discord. As mentioned in the overview, it makes uses of the OpenAI API (specifically the chat completion functionality)

#### Prompt:
![Alt text](README_ASSETS/Prompt.png)

#### Bot thinking:
![Alt text](README_ASSETS/Thinking.png)

#### Response:
![Alt text](README_ASSETS/response.png)

#### Reference to message history:
![Alt text](README_ASSETS/message_history.png)
