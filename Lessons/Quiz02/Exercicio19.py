import csv

def calcular_soma_vendas_por_vendedor(nome_arquivo_csv):
    vendas_por_vendedor = {}
    
    try:
        with open(nome_arquivo_csv, 'r', newline='') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                vendedor = linha['Vendedor']
                venda = int(linha['Venda'])
                vendas_por_vendedor[vendedor] = vendas_por_vendedor.get(vendedor, 0) + venda
            
            return vendas_por_vendedor
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None

nome_arquivo_csv = 'vendas.csv'  
soma_vendas_por_vendedor = calcular_soma_vendas_por_vendedor(nome_arquivo_csv)
if soma_vendas_por_vendedor:
    print("Soma de vendas por vendedor:")
    for vendedor, soma_vendas in soma_vendas_por_vendedor.items():
        print(f"{vendedor}: {soma_vendas}")
