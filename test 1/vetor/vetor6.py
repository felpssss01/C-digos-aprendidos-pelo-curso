import os
os.system("cls")

notas =[9,8,9,10,6]

for nota in notas:
    if n > nota:
        n = nota
    if y < nota:
        y = nota
        
print(f"menor nota: {n}")
print(f"maior nota: {y}")