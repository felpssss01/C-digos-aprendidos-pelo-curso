import os
os.system("cls")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    for valor in linha:
        print(valor, end="\t")
    print()

# o end="\t" é usado para imprimir os valores da matriz separados por uma tabulação, em vez de uma nova linha. Isso faz com que os valores de cada linha da matriz sejam impressos na mesma linha, separados por espaços de tabulação. O print() no final da linha é usado para pular para a próxima linha após imprimir todos os valores de uma linha da matriz.