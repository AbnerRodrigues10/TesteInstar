import re
from datetime import datetime

def processa_etapa2(dados):
    #Converte data em string para o formato SQL "yyyy-mm-dd hh:mm:ss"
    
    def _converter(texto):
        # Procurar padrão de datas no formato dd/mm/aaaa ou dd/mm/aaaa hh:mm:ss
        pattern = r"\b\d{2}/\d{2}/\d{4}(?: \d{2}:\d{2}:\d{2})?\b"

        def _callback(match):
            date_str = match.group(0)
            try:
                if ' ' in date_str:
                    dt = datetime.strptime(date_str, "%d/%m/%Y %H:%M:%S")
                    return dt.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    dt = datetime.strptime(date_str, "%d/%m/%Y")
                    return dt.strftime("%Y-%m-%d 00:00:00")
            except ValueError:
                return date_str

        return re.sub(pattern, _callback, texto)

    # Agora a parte recursiva:
    if isinstance(dados, str):
        return _converter(dados)
    elif isinstance(dados, list):
        return [processa_etapa2(item) for item in dados]
    elif isinstance(dados, dict):
        return {chave: processa_etapa2(valor) for chave, valor in dados.items()}
    else:
        return dados
