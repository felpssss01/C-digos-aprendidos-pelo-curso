import os
os.system("cls")

usuario = []

for i in range(10):
    usuario.append(int(input("Digite um número: ")))
    usuario.sort()

procurado = int(input("Digite o número que deseja procurar: "))

inicio = 0
fim = len(usuario) - 1
encontrado = False

while inicio <= fim:
    meio = (inicio + fim) // 2
    if usuario[meio] == procurado:
        encontrado = True
        print(f"Encontrado na posição {meio}")
        break
    elif procurado < usuario[meio]:
        fim = meio - 1
    else:
        inicio = meio + 1
if not encontrado:
    print("Valor não encontrado")
print("Programa finalizado")

