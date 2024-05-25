def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha.strip())  
    except FileNotFoundError:
        print("Arquivo não encontrado.")

nome_arquivo = 'arquivo.txt'  
ler_arquivo(nome_arquivo)
