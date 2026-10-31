import os
os.system("cls")

nomes = []
notas = []

qtde = int(input("Digite a quantidade de alunos: "))

for i in range(qtde):
    nome = input("Digite o nome do aluno: ")

    notas_aluno = []
    for j in range(4):
        nota = float(input("Digite a nota do aluno: "))
        notas_aluno.append(nota)

    nomes.append(nome)
    notas.append(notas_aluno)

for i in range(qtde):
    media = sum(notas[i]) / 4

    print("\n--- RESULTADO DO ALUNO ---")
    print(f"Nome: {nomes[i]}")
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado")
    elif media >= 5:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")