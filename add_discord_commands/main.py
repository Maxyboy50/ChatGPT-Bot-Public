import requests
import os
from dotenv import load_dotenv
import json
load_dotenv(dotenv_path='./.env')
BOT_TOKEN = os.getenv('BOT_TOKEN')
APPLICATION_ID = "1108091286256369766"
guild_id       = "1073753791440093234"

command_id = "1109334623894388777"
list_commands = f"https://discord.com/api/v10/applications/{APPLICATION_ID}/commands"
delete_url_guild = f"https://discord.com/api/v10/applications/{APPLICATION_ID}/guilds/{guild_id}/commands/{command_id}"
delete_url_global= f"https://discord.com/api/v10/applications/{APPLICATION_ID}/commands/{command_id}"

guild_url_add= f"https://discord.com/api/v10/applications/{APPLICATION_ID}/guilds/{guild_id}/commands" #Add Guild Command
body = {
  "name": "chatgptprompt",
  "description": "Enter a prompt to interact with ChatGPT. This bot is aware of conversational history.",
  "options": [
    {
      "name": "prompt",
      "description": "What you want to ask ChatGPT.",
      "type": 3,
      "required": True
    }
  ],
  "type": 1
}


headers = {
    "Authorization": f"Bot {BOT_TOKEN}"
}

create = requests.post(guild_url_add, headers=headers, json=body)