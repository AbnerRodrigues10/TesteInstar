# Etapa 3: Substituição de Marcadores:
from datetime import datetime

def processa_etapa3(dados):
    for item in dados:
        if "titulo" in item and "dataRealizacao" in item:
            titulo = item["titulo"]
            if isinstance(titulo, str) and "..." in titulo:
                try:
                    # Converte data de "dataRealizacao" (no formato SQL)
                    dt = datetime.strptime(item["dataRealizacao"], "%Y-%m-%d %H:%M:%S")
                    formatted_date = dt.strftime("%d/%m/%Y")
                    formatted_time = dt.strftime("%H:%M:%S")
                    # Substitui os dois marcadores "..." na ordem: primeiro para a data e segundo para a hora.
                    titulo_format = titulo.replace("...", "{}", 1).replace("...", "{}", 1)
                    novo_titulo = titulo_format.format(formatted_date, formatted_time)
                    item["titulo"] = novo_titulo.strip()
                except Exception as e:
                    # Se houver erro, mantém o título.
                    pass
    return dados
