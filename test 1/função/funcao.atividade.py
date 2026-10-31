import os
os.system("cls")

def limpa():
    os.system("cls")

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def definir_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    return "Reprovado"

def mostrar_resultado(nome, media, situacao):
    print("-" *30)
    print("BOLETIM ESCOLAR")
    print("-" *30)
    print(f"Nome: {nome}")
    print(f"Média: {media: .2f}")
    print(f"Situação: {situacao}")

nome = input("Digite o nome do aluno: ").lower()
limpa()

calcular_media_resultado = calcular_media(float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: ")), float(input("Digite a terceira nota: ")))
limpa()

situacao_resultado = definir_situacao(calcular_media_resultado)

mostrar_resultado(nome, calcular_media_resultado, situacao_resultado)