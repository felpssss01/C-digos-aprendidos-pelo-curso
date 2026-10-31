import os
os.system("cls")

notas = [8.5, 7.0, 6.5, 9.0]

soma = 0

for nota in notas:
    soma = soma + nota
media = soma / len(notas)
print(f"Média: {media:.2f}")