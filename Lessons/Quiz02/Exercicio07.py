def intersecao_listas(lista1, lista2):
    intersecao = []
    
    for item in lista1:
        if item in lista2 and item not in intersecao:
            intersecao.append(item)
    
    return intersecao

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
resultado = intersecao_listas(lista1, lista2)
print("Interseção das duas listas:", resultado)
