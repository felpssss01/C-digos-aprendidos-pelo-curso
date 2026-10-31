import os
os.system("cls")

def calcular_media(n1, n2):
    return (n1 + n2) / 2

def situacao(media):
    if media >= 7:
        return "Aprovado"
    return "Reprovado"

media = calcular_media(float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: ")))
print(situacao(media))