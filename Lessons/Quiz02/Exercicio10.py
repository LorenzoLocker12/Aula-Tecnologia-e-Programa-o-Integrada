def calcular_frequencia(texto, palavra):
    palavras = texto.split()
    
    contador = 0
    
    for p in palavras:
        p = p.strip('.,?!')
        if p == palavra:
            contador += 1
    
    return contador

texto = "Este é um exemplo de texto. Neste texto, vamos contar quantas vezes a palavra exemplo aparece."
palavra_desejada = "exemplo"
frequencia = calcular_frequencia(texto, palavra_desejada)
print(f"A palavra '{palavra_desejada}' aparece {frequencia} vezes no texto.")
