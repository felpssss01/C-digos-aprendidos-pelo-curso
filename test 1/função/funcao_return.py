import os
os.system("cls")

def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

resultado = calcular_media(float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: ")))

print(f"A média é: {resultado}")