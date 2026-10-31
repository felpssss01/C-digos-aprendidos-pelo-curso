import os
os.system("cls") #limpa a tela do terminal

nomeP = input("Digite o nome do produto: ")
categoria = input("Digite qual é a categoria do produto: ")
preco = input("Digite o preço do produto: ")
qtdes = input("Digite a quantidade que tem em estoque: ")

print("\n--- Cadastrado ---")
print(f"Nome Do produto: {nomeP}")
print(f"Categoria: {categoria}")
print(f"Preço: R$ {preco}")
print(f"Quantidade em estoque: {qtdes}")