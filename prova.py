import json
import openai

anime=""
episode=""
season=""
extratags=""

def setAnime(title):
    global anime
    anime = title

def setEpisode(episodenumber):
    global episode
    episode = str(episodenumber)

def setSeason(seasonnumber):
    global season
    season = str(seasonnumber)

def getAnime():
    return anime

def getEpisode():
    return episode

def getSeason():
    return season

def getExtratags():
    return extratags


with open("secrets.json") as f:
    secrets = json.load(f)
    api_key = secrets["api_chatgpt_key"]

openai.api_key = api_key

def get_response_anime(messages:list):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages,
        temperature = 1.0 # 0.0 - 2.0
    )
    return response.choices[0].message

def get_response_manga(messages:list):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages,
        temperature = 1.0 # 0.0 - 2.0
    )
    return response.choices[0].message

def searchAnime():
    global anime
    global episode
    global season
    global extratags
    messages = [
        {"role": "system", "content": "Sei un assistente che funziona su un bot telegram e deve rispondere ad ogni frase ricevuta. Sei stato creato per il progetto di Ingegneria del software 2022/2023 da Filippo Notari"}
    ]
    if(str(season).isnumeric()):
        user_input='Anime:'+anime+' Episodio '+episode+' stagione '+season
    else:
        user_input='Anime:'+anime+' Episodio '+episode+' stagione 1'
    messages.append({"role": "user", "content": user_input})
    new_message = get_response_anime(messages=messages)
    response=new_message['content']
    return response