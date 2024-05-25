import csv

def mes_com_menos_vendas(nome_arquivo_csv):
    vendas_por_mes = {}
    
    try:
        with open(nome_arquivo_csv, 'r', newline='') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                mes = linha['Mês']
                vendas = int(linha['Vendas'])
                vendas_por_mes[mes] = vendas_por_mes.get(mes, 0) + vendas
            
         
            mes_menos_vendas = min(vendas_por_mes, key=vendas_por_mes.get)
            total_vendas = vendas_por_mes[mes_menos_vendas]
            
            return mes_menos_vendas, total_vendas
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None, None

nome_arquivo_csv = 'vendas.csv'  
mes, total_vendas = mes_com_menos_vendas(nome_arquivo_csv)
if mes:
    print(f"O mês com menos vendas foi {mes} com um total de vendas de {total_vendas}.")
