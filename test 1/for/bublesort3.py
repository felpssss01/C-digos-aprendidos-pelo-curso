import os  
os.system("cls")

numeros = [6,4,7,2,1,3,5,9]

print(f"O vetor começou com {numeros}")

for i in range(len(numeros)):
    for j in range(len(numeros) - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print(f"O vetor terminou com {numeros}")

