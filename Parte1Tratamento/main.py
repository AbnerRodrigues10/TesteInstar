import leitura
import etapa1
import etapa2
import etapa3
import etapa4
import etapa5
import pprint
import json  # Importa o módulo json para salvar o arquivo

 
def funil(dados):
    
    print("Dados iniciais:")
    
    dados1 = etapa1.processa_etapa1(dados)
    print("\nApós etapa 1 (Retirar espaços NBSP):")
    print (json.dumps(dados1, ensure_ascii=False, indent=2))

    dados2 = etapa2.processa_etapa2(dados1)
    print("\nApós etapa 2 (Conversão de Data):")
    print (json.dumps(dados2, ensure_ascii=False, indent=2))

    
    dados3 = etapa3.processa_etapa3(dados2)
    print("\nApós etapa 3 (Substituição de Marcadores):")
    print (json.dumps(dados3, ensure_ascii=False, indent=2))
    

    dados4 = etapa4.processa_etapa4(dados3)
    print("\nApós etapa 4 (Transformação de Lista em String):")
    print (json.dumps(dados4, ensure_ascii=False, indent=2))
    

    dados5 = etapa5.processa_etapa5(dados4)
    print("\nApós etapa 5 (Exclusão de chaves com valores nulos):")
    print (json.dumps(dados5, ensure_ascii=False, indent=2))


    print("Exibindo o arquivo usando formatação JSON")
    Dadofinal = json.dumps(dados5, ensure_ascii=False, indent=2)
    
    return Dadofinal

if __name__ == "__main__":
    dadosRecebidos = leitura.carregar_json("entrada.json")
    
    if dadosRecebidos is not None:
        resultado = funil(dadosRecebidos)
        print("\nDados finais retornados pelo pipeline:")
        pprint.pprint(resultado)
        
        # Salva o resultado final em um arquivo chamado "saida.json"
        with open("saida.json", "w", encoding="utf-8") as arquivo_saida:
            arquivo_saida.write(resultado)
    else:
        print("Falha ao carregar os dados. Verifique o arquivo 'entrada.json'.")
