import os
os.system("cls")

#len lê o tamanho do vetor, e o for percorre o vetor, comparando os elementos adjacentes. Se o elemento da esquerda for maior que o da direita, eles são trocados de posição. Esse processo é repetido até que todos os elementos estejam ordenados.

numeros = [5, 3, 8, 2]
for i in range(len(numeros)):
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
print(numeros)