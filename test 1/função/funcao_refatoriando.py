import os
os.system("cls")

def limpar_tela():
    os.system("cls")

def mostrar_menu():
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Alterar preço do produto")
    print("5 - Entrada de estoque")
    print("6 - Saída de estoque")
    print("0 - Sair")

def cadastrar_produto(produtos):
    codigo = input("Código do produto: ")
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade em estoque: "))
    produtos[nome] = {"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade}
    print(f"Produto {nome} cadastrado com sucesso!")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("Produtos Cadastrados.")
        for 



def main():