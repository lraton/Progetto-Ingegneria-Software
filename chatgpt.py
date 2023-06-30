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


def bot(message):
    messages = [
        {"role": "system", "content": "Sei un assistente che funziona su un bot telegram e deve rispondere ad ogni frase ricevuta. Sei stato creato per il progetto di Ingegneria del software 2022/2023 da Filippo Notari"}
    ]
    user_input=message
    messages.append({"role": "user", "content": user_input})
    new_message = get_response(messages=messages)
    response=new_message['content']
    messages.append(new_message)
    print(messages)
    return response