import os
os.system("cls")

senha = input("Digite a senha: ")

while senha != "1234":
    print("Senha incorreta!")
    senha = input("Digite a senha novamente: ")

print("Acesso liberado!")
