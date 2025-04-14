import json

#1.	Remoção de Espaçamentos e Erros de NBSP
def processa_etapa1(dados):
    
    # Define as chaves a serem tratadas
    campos = ["nome", "sobrenome", "titulo"]

    # um for para indenficar os compos "nome", "sobrenome", "titulo"
    for item in dados:
        for campo in campos:
            if campo in item and isinstance(item[campo], str):
                # •	Substitua os caracteres de espaço não quebra (NBSP) por espaços normais.
                item[campo] = item[campo].replace('\u00a0', ' ').strip()
    
    return dados