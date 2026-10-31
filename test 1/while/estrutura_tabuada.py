import os
os.system("cls")

n = int(input("Informe um número: "))
t = 0
c = 0

print(f"Tabuado do {n}")
while c <= 10:
    t = n * c
    print(f"{n} X {c} = {t}")
    c += 1
print("Programa finalizado...")