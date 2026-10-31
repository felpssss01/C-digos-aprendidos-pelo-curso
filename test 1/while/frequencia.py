import os
os.system("cls")

nome = str(input("Qual é o seu nome estudante? "))

n1 = float(input("Digite a nota do seu primeiro bimestre: "))

n2 = float(input("Digite a nota do segundo bimestre: "))

n3= float(input("Digite a nota do terceiro bimestre: "))

n4 = float(input("Digite a nota do quarto bimestre: "))

frequencia = int(input("Digite a sua frequência: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 7 and frequencia >= 75:
    print("\n --- BOLETIM --- ")
    print(f"Nome: {nome}")
    print("Status: Aprovado")
    print(f"Media: {media: .2f}")
    print(f"Frequência: {frequencia: .2f}")
else:
    print("\n --- BOLETIM --- ")
    print(f"Nome: {nome}")
    print("Status: Reprovado")
    print(f"Media: {media: .2f}")
    print(f"Frequência: {frequencia: .2f}")