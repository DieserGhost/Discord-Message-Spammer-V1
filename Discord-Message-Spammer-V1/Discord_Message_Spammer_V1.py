import json
import requests
import time

print('DiscordMessageSpammer V1 | Sending your Message...')

# Load configuration from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

payload = {
    'content': config["message_content"]
}

header = {
    'authorization': config["authorization_key"]
}

# Function to make 25 POST requests
def make_requests():
    for _ in range(25):
        try:
            response = requests.post(config["api_url"], data=payload, headers=header)
            print(f"Status Code: {response.status_code}, Response: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

# Loop for the total number of iterations
for _ in range(10000):
    make_requests()
    time.sleep(5)
