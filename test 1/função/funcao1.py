import os
os.system("cls")

def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

resultado = calcular_media(float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: ")))

if resultado >= 7:
    print(f"A média é: {resultado} - Aprovado")
else:
    print(f"A média é: {resultado} - Reprovado")
