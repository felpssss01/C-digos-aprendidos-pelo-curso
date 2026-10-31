import os
os.system("cls")

produtos = [
    {"codigo": "1001", "nome": "Computador", "preco": 2642.56, "quantidade": 11, "categoria": "Eletrônicos"},
    {"codigo": "1002", "nome": "Notebook", "preco": 3200.00, "quantidade": 5, "categoria": "Eletrônicos"},
    {"codigo": "1003", "nome": "Impressora", "preco": 500.00, "quantidade": 8, "categoria": "Eletrônicos"},
    {"codigo": "2034", "nome": "Mouse", "preco": 56.67, "quantidade": 18, "categoria": "Eletrônicos"}
]

codigo = input("Informe o código do produto: ")
encontrado = False

for produto in produtos:
    if produto["nome"] == codigo:
        print(produto)
        encontrado = True
        break
if not encontrado:
    print("Produto não encontrado")

valor_estoque = produto["preco"] * produto["quantidade"]
print(f"Valor total em estoque para o produto {produto['nome']}: R$ {valor_estoque:.2f}")
