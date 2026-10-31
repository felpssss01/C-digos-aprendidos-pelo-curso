import os
os.system("cls")

produtos = [
    {"codigo": "1001", "nome": "Computador", "preco": 2642.56, "quantidade": 11, "categoria": "Eletrônicos"},
    {"codigo": "1002", "nome": "Notebook", "preco": 3200.00, "quantidade": 5, "categoria": "Eletrônicos"},
    {"codigo": "1003", "nome": "Impressora", "preco": 500.00, "quantidade": 8, "categoria": "Eletrônicos"},
    {"codigo": "2034", "nome": "Mouse", "preco": 56.67, "quantidade": 18, "categoria": "Eletrônicos"}
]

def limpa_tela():
    os.system("cls")

def buscar_produto(produtos, codigo):
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None

codigo = input("Informe o código do produto: ")

resultado = buscar_produto(produtos, codigo)

limpa_tela()

if resultado is not None:
    print("Produto encontrado:")
    print(f"Código: {resultado['codigo']}")
    print(f"Nome: {resultado['nome']}")
    print(f"Preço: R$ {resultado['preco']:.2f}")
    print(f"Quantidade: {resultado['quantidade']}")
    print(f"Categoria: {resultado['categoria']}")
else:
    print("Produto não encontrado.")