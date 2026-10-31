import os
os.system("cls")

n = int(input("Digite um número: "))

for c in range(1, 11):
    t = n * c
    print(f" {n} X {c} = {t}")
