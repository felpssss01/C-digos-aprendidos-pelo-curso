import os
os.system("cls")

alunos = [
    {"nome": "Ana", "media": 8.0},
    {"nome": "Bruno", "media": 6.5},
    {"nome": "Carla", "media": 9.0}
]

for aluno in alunos:
    print("Nome:", aluno["nome"])
    print("Média:", aluno["media"])
    print()

for linha in alunos:
    for valor in linha:
        print(valor, end="\t")
    print()
    