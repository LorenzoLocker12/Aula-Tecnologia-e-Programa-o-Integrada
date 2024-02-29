def k_maiores_elementos(lista, k):
    sorted_lista = sorted(lista, reverse=True)
    k_maiores = sorted_lista[:k]
    return k_maiores

lista = [4, 8, 2, 6, 1, 9, 5, 3, 7]
k = 3
maiores_elementos = k_maiores_elementos(lista, k)
print(f"Os {k} maiores elementos na lista são:", maiores_elementos)
