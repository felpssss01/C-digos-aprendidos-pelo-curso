import os
os.system("cls")

matriz = [[14,43,56,22], [12,34,56,78], [11,22,33,44]]

print("Número de linhas:", len(matriz))
print("Número de colunas:", len(matriz[0]))
print(matriz[0][0])
print(matriz[1][2])
print(matriz[2][3])
print("Matriz completa:")
for linha in matriz:
    for valor in linha:
        print(valor, end="\t")
    print()