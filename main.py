from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def carregar_personalidade():
    try:
        with open("personality.txt", "r", encoding="utf-8") as file:
            return file.read()
    except:
        return "Você é Nex Assistant, assistente pessoal de Lexi."

def carregar_memoria():
    if os.path.exists("memory.json"):
        with open("memory.json", "r") as file:
            return json.load(file)
    return {}

def responder(pergunta):
    personalidade = carregar_personalidade()

    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": personalidade},
            {"role": "user", "content": pergunta}
        ]
    )

    return resposta.choices[0].message.content

def main():
    print("Nex Assistant conectado à IA.")

    while True:
        entrada = input("Você: ")
        resposta = responder(entrada)
        print("Nex:", resposta)

if __name__ == "__main__":
    main()
