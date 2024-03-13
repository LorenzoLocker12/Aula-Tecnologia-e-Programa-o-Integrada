import os

def consolidar_arquivos_diretorio(diretorio, arquivo_saida):
    try:
        with open(arquivo_saida, 'w') as saida:
            for nome_arquivo in os.listdir(diretorio):
                caminho_arquivo = os.path.join(diretorio, nome_arquivo)
                if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith('.txt'):
                    with open(caminho_arquivo, 'r') as arquivo:
                        saida.write(f"Conteúdo do arquivo: {nome_arquivo}\n")
                        saida.write(arquivo.read())
                        saida.write('\n\n')  
        print("Consolidação concluída. Arquivo de saída:", arquivo_saida)
    except FileNotFoundError:
        print("Diretório não encontrado.")

diretorio = '/caminho/para/diretorio'  
arquivo_saida = 'consolidado.txt' 
consolidar_arquivos_diretorio(diretorio, arquivo_saida)