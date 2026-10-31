import os
os.system("cls")

alunos = []

for i in range(3):
    aluno = {}

    aluno["nome"] = input("Nome: ")
    aluno["media"] = float(input("Média: "))

    alunos.append(aluno)

print("\n")

for aluno in alunos:
    print(aluno["nome"], aluno["media"])