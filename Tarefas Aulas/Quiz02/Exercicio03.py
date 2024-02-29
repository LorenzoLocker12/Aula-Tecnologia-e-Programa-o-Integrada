def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

frase = "Esta é uma frase de exemplo para contar palavras."
numero_de_palavras = contar_palavras(frase)
print("Número de palavras na frase:", numero_de_palavras)
