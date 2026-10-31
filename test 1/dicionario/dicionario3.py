import os
os.system("cls")

alunos = [
    {"nome": "Ana", "media": 8.0},
    {"nome": "Bruno", "media": 6.5},
    {"nome": "Carla", "media": 9.0}
]

print(alunos[0])
print(alunos[0]["nome"])

for aluno in alunos:
    print(aluno["nome"], aluno["media"])
