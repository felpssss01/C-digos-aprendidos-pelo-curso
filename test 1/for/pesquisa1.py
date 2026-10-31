import os
os.system("cls")

numeros = [10, 25, 3, 18, 40]
procurado = 40
d = 0
for i in range(len(numeros)):
    d = d + 2
    if numeros[i] == procurado:
        print(f"Encontrado na posição {i}")
        break


