import os
def limpa():
    os.system("cls")


produtos = []

for i in range (2):
    print("-"*30)
    print(f"Produto {i + 1}")
    print("-"*30)
    print("\n")

    produto = {}

    produto["nome"] = input("Nome do produto: ")
    produto["preco"] = float(input("Preço do produto: "))
    produto["quantidade"] = int(input("Quantidade do produto: "))
    produto["codigo"] = int(input("Código do produto: "))

    produtos.append(produto)
limpa()

print("\n")

codigo = int(input("Digite o código do produto que deseja procurar: "))

for busca in(produtos):
    if busca["codigo"] == codigo:
        print("\n")
        print("-"*30)
        print("Produto encontrado!")
        print("-"*30)
        print(f"\nQuantidade atual do produto {busca['nome']}: {busca['quantidade']}")
        u = int(input("Digite a quantiddade que deseja adicionar ao estoque: "))
        print("\n")
        busca["quantidade"] += u
        print(f"Unidades adicionadas: {u}")
        print(f"Estoque atualizado: {busca['quantidade']}")
        break
    else:
        print("Produto não encontrado.")


print("Sistema finalizado.")