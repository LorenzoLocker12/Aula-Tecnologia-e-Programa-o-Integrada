def soma_matrizes(matriz1, matriz2):
    # Verificando se as duas matrizes têm o mesmo tamanho
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("As matrizes têm tamanhos diferentes. Não é possível realizar a soma.")
        return None
    
    resultado = []
    
    for i in range(len(matriz1)):
        linha_resultado = []
        for j in range(len(matriz1[0])):
            soma = matriz1[i][j] + matriz2[i][j]
            linha_resultado.append(soma)
        resultado.append(linha_resultado)
    
    return resultado

matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

resultado = soma_matrizes(matriz1, matriz2)
if resultado:
    print("Resultado da soma das matrizes:")
    for linha in resultado:
        print(linha)
