from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))
chat = client.chats.create(model="gemini-3-flash-preview")

def enviar_msg(user_input: str):
    response = chat.send_message(
        message=user_input,
        config=types.GenerateContentConfig(
            system_instruction="Responda de forma simplificada"
        )
    )
    return response.text

print("Chat iniciado!\n")
while True:
    user_input = input("Voce: ")
    if user_input.lower() == "sair":
        break
    try:
        response = enviar_msg(user_input)
        print(f"Assistente: {response}\n")
    except:
        print("Falha ao gerar resposta")
        break

