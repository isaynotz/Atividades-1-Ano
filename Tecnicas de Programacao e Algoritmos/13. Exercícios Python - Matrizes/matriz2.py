#51 - Crie um programa que crie uma matriz de dimensão 5x5 e preencha com valores lidos pelo teclado.
#A - Mostre a matriz na tela, com a formatação correta.
#B - Mostre a soma de todos os números ímpares digitados.
#C - Mostre a soma dos valores da primeira coluna.
#D - Mostre a soma dos valores da quinta linha.
#E - O menor valor da segunda coluna.

matriz= [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

somaimpar = somacoluna1 = somalinha5 = 0

for linha in range(0,5):
    for coluna in range(0,5):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha}, {coluna}]'))

for linha in range(0,5):
    for coluna in range(0,5):
        if matriz[linha][coluna] %2 == 1:
            somaimpar += matriz[linha][coluna]
        print(f'[{matriz[linha][coluna]:^5}]')
    print('')

for linha in range(0,5):
    somacoluna1 += matriz[linha][0]

for coluna in range(0,5):
    somalinha5 += matriz[4][coluna]
