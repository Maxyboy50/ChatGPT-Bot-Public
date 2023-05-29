# Serverless ChatGPT Bot

## Overview:
This purpose of this project was to integrate the incredibly powerful OpenAI API with the popular community platform Discord to provide ChatGPT-like functionality from within the platform. The bot can respond to any prompt and has the ability to remember message history (a feature not included in the OpenAI API natively).

### Technologies used:
The code for this bot is written entirely in Python and leverages AWS API Gateway, AWS Lambda, and AWS DynamoDB for receiving, processing, and storing events received from Discord. As mentioned in the overview, it makes uses of the OpenAI API (specifically the chat completion functionality).

I use Terraform to deploy the deploy all of the underlying infrastructure on AWS

### Examples:
#### Prompt:
![Alt text](README_ASSETS/Prompt.png)

#### Bot thinking:
![Alt text](README_ASSETS/Thinking.png)

#### Response:
![Alt text](README_ASSETS/response.png)

#### Reference to message history:
![Alt text](README_ASSETS/message_history.png)
