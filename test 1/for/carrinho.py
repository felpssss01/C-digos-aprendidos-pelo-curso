import os
os.system("cls")

p = input("Quantos produtos você deseja comprar: ")

precos = []
for i in range(int(p)):
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    precos.append(preco)
    print(f"O produto {produto} custa R$ {preco: .2f}")

total = sum(precos)

print(f"O total da compra é: R$ {total: .2f}")