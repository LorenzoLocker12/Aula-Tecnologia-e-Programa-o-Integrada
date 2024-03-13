import csv

def ler_arquivo_csv(nome_arquivo):
    try:
        with open(nome_arquivo, newline='') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv, delimiter=',')
            for linha in leitor_csv:
                print(linha)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

nome_arquivo_csv = 'dados.csv' 
ler_arquivo_csv(nome_arquivo_csv)
