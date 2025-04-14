# Etapa 4: Transformação de Lista em String
def processa_etapa4(dados):
    for item in dados:
        if "descricao" in item and isinstance(item["descricao"], list):
            # Concatena os elementos da lista em uma única string, separando-os por um espaço.
            item["descricao"] = " ".join(item["descricao"]).strip()
    return dados
