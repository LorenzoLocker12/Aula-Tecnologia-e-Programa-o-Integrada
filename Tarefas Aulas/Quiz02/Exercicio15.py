import json

def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo) as arquivo_json:
            dados = json.load(arquivo_json)
            return dados
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None

nome_arquivo_json = 'dados.json'  
dados_json = ler_arquivo_json(nome_arquivo_json)
if dados_json:
    print("Conteúdo do arquivo JSON:")
    print(dados_json)
