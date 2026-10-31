import os
os.system("cls")

def limpa():
    os.system("cls")

def somar(n1,n2):
    return n1 + n2

r1 = somar(float(input("Digite o primeiro número que você deseja somar: ")), float(input("Digite o segundo número que você deseja somar: ")))

limpa()

def subtrair(n3,n4):
    return n3 - n4

r2 = subtrair(float(input("Digite o primeiro número que você deseja subtrair: ")), float(input("Digite o segundo número que você deseja subtrair: ")))

limpa()

def multiplicar(n5,n6):
    return n5 * n6

r3 = multiplicar(float(input("Digite o primeiro número que você deseja multiplicar: ")), float(input("Digite o segundo número que você deseja multiplicar: ")))

limpa()

def dividir(n7,n8):
    if n8 == 0:
        return "Não é possível dividir por zero"
    else:
        return n7 / n8

r4 = dividir(float(input("Digite o primeiro número que você deseja dividir: ")), float(input("Digite o segundo número que você deseja dividir: ")))

limpa()

print("#"*10)
print("RESULTADOS")
print("#"*10)

print("\n")

print(f"Somar: {r1}")
print(f"Subtrair: {r2}")
print(f"Multiplicar: {r3}")
print(f"Dividir: {r4}")
