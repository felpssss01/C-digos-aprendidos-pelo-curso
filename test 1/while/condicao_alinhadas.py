import os
os.system("cls")
usuario = str(input("Digite o nome do usuário: "))

if usuario == "admin":
    senha = input("Digite a senha: ")
    if senha == "1234":
        print("\n --- LOGIN ---")
        print("Acesso permitido")
    else:
        print("\n --- LOGIN --- ")
        print("Senha incoreta")
else:
    print("\n --- LOGIN --- ")
    print("Usuário não encontrado")