def contar_ocorrencias(frase, palavra):
    palavras_na_frase = frase.split()
    
    contador = 0
    
    for palavra_na_frase in palavras_na_frase:
        if palavra_na_frase == palavra:
            contador += 1
    
    return contador

frase = "Esta é uma frase de exemplo com a palavra repetida várias vezes."
palavra = "palavra"
numero_de_ocorrencias = contar_ocorrencias(frase, palavra)
print(f"A palavra '{palavra}' ocorre {numero_de_ocorrencias} vezes na frase.")
