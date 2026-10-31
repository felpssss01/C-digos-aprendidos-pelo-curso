import os
os.system("cls")

alunos = ["Pedro", "Heitor", "Ana", "Gustavo", "Claudio", "Felipe"]

nome = input("Digite o nome do aluno: ")

if nome in alunos:
    print("Nome encontrado na lista de alunos.")
else:
    print("Nome não encontrado.")