import requests
import json

QUILLBOT_API_URL = "https://api.quillbot.com/api/paraphrase/singleParaphrase"

def check_spelling(text):
    payload = {
        "text": text,
        "mode": "standard",
        "dialect": "us",
        "intent": "checking",
        "appKey": "YOUR_APP_KEY" # Replace with your own Quillbot app key
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(QUILLBOT_API_URL, data=json.dumps(payload), headers=headers)
    if response.ok:
        data = response.json()
        return data["paraphrasedText"]
    else:
        response.raise_for_status()
