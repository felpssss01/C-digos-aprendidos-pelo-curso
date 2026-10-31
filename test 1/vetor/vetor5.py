import os
os.system("cls")

notas = [8, 10, 9, 7]
maior = notas[0]
for nota in notas:
 if nota > maior:
  maior = nota
print(f"Maior nota: {maior}")