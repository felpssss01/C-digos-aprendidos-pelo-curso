import os
os.system("cls")

n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua nota: "))

media = ( n1 + n2 ) / 2

if media >= 7:
    print("\n --- Aprovado --- ")
    print(f"Sua nota é: {media}")
else:
    print("\n --- Reprovado ---")
    print(f"Sua nota é: {media}")