import os
os.system("cls")

c = 1
soma = 0

while c <=5 :
    n = int(input(f"Digite um número: "))
    soma += n
    c +=1
print(f"O total dos números é {soma}")
