import json
import openai

with open("secrets.json") as f:
    secrets = json.load(f)
    api_key = secrets["api_chatgpt_key"]

openai.api_key = api_key

def get_response(messages:list):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages,
        temperature = 1.0 # 0.0 - 2.0
    )
    return response.choices[0].message