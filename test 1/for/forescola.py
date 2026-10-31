import os
os.system("cls")

notas = []
for i in range(4):
    nota = float(input("Digite nota do aluno: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"A média do aluno é: {media: .2f}")

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado") 