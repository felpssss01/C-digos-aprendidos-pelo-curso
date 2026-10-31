import os
os.system("cls")

produtos = ["Arroz", "Feijão", "Macarrão", "Carne", "Frango", "Leite", "Ovos", "Pão", "Queijo", "Manteiga"]

busca = input("Digite o nome do produto: ")

posicao = -1

for indice in range(len(produtos)):
    if produtos[indice] == busca:
        posicao = indice
if posicao != -1:
    print(f"O produto foi encontrado no índice {posicao}")
else:
    print("Produto não encontrado.")
