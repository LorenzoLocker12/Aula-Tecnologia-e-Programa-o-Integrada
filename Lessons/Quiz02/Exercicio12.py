def encontrar_menor_string(lista):
    if not lista:
        return None
    
    menor_string = lista[0]
    
    for string in lista:
        if len(string) < len(menor_string):
            menor_string = string
    
    return menor_string

lista_de_strings = ["banana", "abacaxi", "uva", "laranja", "maçã"]
menor_string = encontrar_menor_string(lista_de_strings)
print("A menor string na lista é:", menor_string)
