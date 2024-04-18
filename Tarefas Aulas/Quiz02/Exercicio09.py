def encontrar_pares_soma(lista, alvo):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                pares.append((lista[i], lista[j]))
    return pares

lista = [2, 4, 3, 5, 7, 8, 9]
alvo = 10
pares = encontrar_pares_soma(lista, alvo)
print("Pares cuja soma é igual a", alvo, ":", pares)
