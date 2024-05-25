lista = input("Digite a lista")

lista = lista.lower()
vogais = 0
consoantes = 0

for i in lista:
    if i in ['a', 'e', 'i', 'o', 'u']:
        vogais += 1
    else:
        consoantes += 1

print(f'Existem {vogais} vogais e {consoantes} consoantes')