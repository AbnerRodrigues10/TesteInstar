# leitura.py
import json

def carregar_json(diretorioJson):
    try:
        with open(diretorioJson, "r", encoding="utf-8") as entrada:
            dados = json.load(entrada)
        return dados
    except Exception as e:
        print("Erro ao abrir ou processar o arquivo:", e)
        return None
