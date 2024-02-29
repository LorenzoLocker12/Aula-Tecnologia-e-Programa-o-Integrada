frase = input("Digite a frase: ")
remover = input("\nDigite a letra que quer substituir: ")
novaLetra = input("\nDigite a letra que quer colocar no local da antiga letra: ")

for i in frase:
    if i in remover:
        frase = frase.replace(remover, novaLetra)

print(f"\n{frase}")