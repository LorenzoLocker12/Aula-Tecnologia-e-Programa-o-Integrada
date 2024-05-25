import csv

def encontrar_vendedores_maximo_e_minimo_vendas(nome_arquivo_csv):
    vendas_por_vendedor = {}
    
    try:
        with open(nome_arquivo_csv, 'r', newline='') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                vendedor = linha['Vendedor']
                venda = int(linha['Venda'])
                vendas_por_vendedor[vendedor] = vendas_por_vendedor.get(vendedor, 0) + venda
            
            vendedor_max_vendas = max(vendas_por_vendedor, key=vendas_por_vendedor.get)
            total_max_vendas = vendas_por_vendedor[vendedor_max_vendas]
            
            vendedor_min_vendas = min(vendas_por_vendedor, key=vendas_por_vendedor.get)
            total_min_vendas = vendas_por_vendedor[vendedor_min_vendas]
            
            return vendedor_max_vendas, total_max_vendas, vendedor_min_vendas, total_min_vendas
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None, None, None, None

# Exemplo de uso:
nome_arquivo_csv = 'vendas.csv'  # Substitua 'vendas.csv' pelo caminho do arquivo CSV desejado
vendedor_max_vendas, total_max_vendas, vendedor_min_vendas, total_min_vendas = encontrar_vendedores_maximo_e_minimo_vendas(nome_arquivo_csv)
if vendedor_max_vendas and vendedor_min_vendas:
    print(f"O vendedor que mais vendeu foi {vendedor_max_vendas} com um total de vendas de {total_max_vendas}.")
    print(f"O vendedor que menos vendeu foi {vendedor_min_vendas} com um total de vendas de {total_min_vendas}.")
