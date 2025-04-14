# Etapa 5: Exclusão de chaves com valores nulos:
def processa_etapa5(dados):
    def remove_null(data):
        
        if isinstance(data, dict):
            return {
                chave: remove_null(valor) 
                for chave, valor in data.items()
                if valor is not None
                } 
        elif isinstance(data, list):
            return [remove_null(item) for item in data]
        else:
            return data

    return remove_null(dados)
