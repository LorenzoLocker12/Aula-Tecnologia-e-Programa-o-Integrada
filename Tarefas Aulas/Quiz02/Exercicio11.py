def is_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def numeros_primos(lista):
    primos = []
    for num in lista:
        if is_primo(num):
            primos.append(num)
    return primos

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primos = numeros_primos(numeros)
print("Números primos na lista:", primos)
