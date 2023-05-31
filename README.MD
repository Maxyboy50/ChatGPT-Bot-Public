# Serverless ChatGPT Discord Bot

## Overview:
This purpose of this project was to integrate the incredibly powerful OpenAI API with the popular community platform Discord to provide ChatGPT-like functionality from within the platform. The bot can respond to any prompt and has the ability to recall previously sent messages (a feature not included in the OpenAI API natively).

I decided to make this bot serverless due to the event based nature of Discord bots; they are only invoked upon slash commands

### Technologies used:
- The code for this bot is written entirely in Python.
- AWS API Gateway, AWS Lambda, and AWS DynamoDB along with other complimentary services (eg. IAM).
- Terraform for deploying/managing the infrastructure.
- Azure DevOps pipeline for CI/CD.


### Examples:
#### Prompt:
![Alt text](README_ASSETS/Prompt.png)

#### Bot thinking:
![Alt text](README_ASSETS/Thinking.png)

#### Response:
![Alt text](README_ASSETS/response.png)

#### Reference to message history:
![Alt text](README_ASSETS/message_history.png)
