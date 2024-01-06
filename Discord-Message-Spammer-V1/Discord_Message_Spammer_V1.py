import json
import requests


print('DiscordMessageSpammer V1| Sending your Message...')

with open('config.json') as config_file:
    config = json.load(config_file)

payload = {
    'content': config["message_content"]
}


header = {
  'authorization': config["authorization_key"]  
}

for i in range(10000):
    r = requests.post(config["api_url"], data=payload, headers=header)