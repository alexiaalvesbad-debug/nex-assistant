import json
import os

# carregar personalidade
def carregar_personalidade():
    try:
        with open("personality.txt", "r", encoding="utf-8") as file:
            return file.read()
    except:
        return "Personalidade padrão do Nex Assistant."

# carregar memória
def carregar_memoria():
    if os.path.exists("memory.json"):
        with open("memory.json", "r") as file:
            return json.load(file)
    return {}

# salvar memória
def salvar_memoria(memoria):
    with open("memory.json", "w") as file:
        json.dump(memoria, file)

def responder(usuario_input):
    memoria = carregar_memoria()

    if "nome" in usuario_input.lower():
        memoria["nome_usuario"] = "Lexi"
        salvar_memoria(memoria)
        return "Nome registrado, Lexi."

    return "Estou ativo. Como posso ajudar?"

def main():
    print("Nex Assistant iniciado.")
    personalidade = carregar_personalidade()
    print(personalidade)

    while True:
        entrada = input("Você: ")
        resposta = responder(entrada)
        print("Nex:", resposta)

if __name__ == "__main__":
    main()
