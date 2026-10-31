import os
os.system("cls")

produto = {
    "codigo": "1001",
    "nome": "Computador",
    "preco": 2642.56,
    "quantidade": 11,
    "categoria": "Eletrônicos",

}

print("\n")

print(produto["codigo"])
print(produto["nome"])
print(produto["preco"])
print(produto["quantidade"])
print(produto["categoria"])

produto["quantidade"] = produto["quantidade"] + 10
print(produto["quantidade"])
produto["preco"] = 2000.00
print(produto["preco"])