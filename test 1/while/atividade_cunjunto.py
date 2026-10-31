import os
os.system("cls")

opcao = 0



while opcao !=4:
    print("---Menu---")
    print("1- Somar 2 números")
    print("2 - Verificar se o número é par ou impar")
    print("3 - Mensagem")
    print("4 - Saindo do programa.")
    try:
        opcao = int(input("Selecione a opção: "))

        if opcao == 1:
            numero = int(input("Digite um número: "))
            numero2 = int(input("Digite um número: "))
            print (f" Soma dos dois números é : ", numero + numero2)
            opcao = int(input("Digite 5 para voltar ao menu inicial"))
        elif opcao == 2:
            numero = int(input("Digite um número: "))
            if numero % 2 == 0:
                print("O número é par")
            else:
                print("O número é ímpar")
        elif opcao == 3:
            print("Seja bem-vindo ao Senac, Estudante!!! ")
        elif opcao == 4:
            print("Sair Selecionado.")
        else:
            print("Opção invalida")
    except ValueError:
        print("Aceitamos apenas números...")
