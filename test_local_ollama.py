import requests
import ollama
import asyncio
from ollama import AsyncClient

async def chat():
    message = {'role': 'user', 'content': 'Why is the sky blue?'}
    response = await AsyncClient().chat(model='llama3.1', messages=[message])
    print(response)
asyncio.run(chat())



def test_ollama_server(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Server is reachable. Status code: {response.status_code}")
        else:
            print(f"Server responded with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to reach server. Error: {e}")



# Replace 'http://localhost:5000/' with your actual Ollama server URL
test_ollama_server('http://localhost:11434/')

