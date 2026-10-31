import os
os.system("cls")

alunos = ["Pedro", "Heitor", "Ana", "Gustavo", "Claudio", "Felipe"]
alunos.remove("Ana")
alunos.pop(5)

for indice in range(len(alunos)):
    print(f"O aluno {alunos[indice]} está na posição {indice}")