import os
os.system("cls")

def calcular_media_lista(notas):
    if len(notas) == 0:
        return None  # Evita divisão por zero se a lista estiver vazia
    
    soma = 0

    for nota in notas:
        soma += nota

    return soma / len(notas)

notas = [8.5, 7.0, 9.5]

media = calcular_media_lista(notas)

if media is not None:
    print(f"A média das notas é: {media}")
else:
    print("Não há notas para calcular a média.")