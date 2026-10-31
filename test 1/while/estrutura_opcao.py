import os
os.system("cls")

opcao = 0

while opcao != 4:
    print("1 - Somar dois números")
    print("2 - Verificar se um número é par ou impar")
    print("3 - Mostrar uma mensagem de boas vindas")
    print("4 - Sair")
    

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\n --- Soma dois números selecionado --- ")
        n = int(input("Informe um número: "))
        c = int(input("Informe o segundo número: "))
        t = n + c
        print(f"total da soma: {t: .2f}")
        print("\n")
    elif opcao == 2:
        print("\n --- Verificar número selecionado ---")
        a = int(input("Digite um número: "))
        if a % 2 ==0:
            print(f"{a} é par")
        else:
            print(f"{a} é impar")
        print("\n")
    elif opcao == 3:
        print("\n --- Mostrar mensagem selecionado --- ")
        print("Seja bem-vindo ao Senac")
        print("\n")
    elif opcao == 4:
        print("\n --- Sair Selecionado --- ")
        print("Saindo do programa...")
        print("\n")
    else:
        print("Opção inválida")