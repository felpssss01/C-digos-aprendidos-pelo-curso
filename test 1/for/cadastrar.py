import os
os.system("cls")

nomes = []

notas = []

quantidade = int(input("Quantidade de alunos: "))

for contador in range(quantidade):
    nome = input("Nome: ")
    nota = float(input("Nota: "))
    
    nomes.append(nome)
    notas.append(nota)

for indice in range(len(nomes)):
    print(f"{nomes[indice]} - Nota: {notas[indice]}")