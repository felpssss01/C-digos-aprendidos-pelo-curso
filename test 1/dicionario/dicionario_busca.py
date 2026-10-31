import os
os.system("cls")

alunos = [
    {"nome": "Ana", "media": 8.0, "matricula": "2026001"},
    {"nome": "Bruno", "media": 6.5, "matricula": "2026002"},
    {"nome": "Carla", "media": 9.0, "matricula": "2026003"}
]

matricula_busca = input("Matrícula: ")
encontrado = False

for aluno in alunos:
    if aluno["matricula"] == matricula_busca:
        print(aluno)
        encontrado = True
        break
if not encontrado:
 print("Aluno não encontrado")
