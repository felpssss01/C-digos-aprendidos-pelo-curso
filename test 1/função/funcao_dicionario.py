import os
os.system("cls")

produto = {
    "codigo": "18001",
    "nome": "Arroz",
    "preco": 5.99,
}

def mostrar_produto(produto):
    print(f"Código: {produto['codigo']}")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")

mostrar_produto(produto)