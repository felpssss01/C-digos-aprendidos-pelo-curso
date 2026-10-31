import os
os.system("cls")   

import os
os.system("cls")

quantidade = int(input("Quantos produtos? "))
total = 0

for i in range(quantidade):
    nome = input(f"Informe o nome do produto {i + 1}: ")
    preco = float(input("Informe o preço: R$ "))
    total += preco

print(f"O total a pagar é: R$ {total}")