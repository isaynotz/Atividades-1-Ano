#50 - Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#A - Mostre a matriz na tela, com a formatação correta.
#B - Mostre a soma de todos os números pares digitados.
#C - Mostre a soma dos valores da segunda coluna.
#D - Mostre a soma dos valores da terceira coluna.
#E - O maior valor da segunda linha.


matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

somapar = somacoluna2 = somacoluna3 = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]'))

for linha in range(0,3):
    for coluna in range(0,3):
        if matriz[linha][coluna] %2 == 0:
            somapar += matriz[linha][coluna]
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print('')
print('-='*30)

for linha in range(0,3):
    somacoluna2 += matriz[linha][1]
    somacoluna3 += matriz[linha][2]

print(f'A soma dos números pares é {somapar}')
print(f'A soma dos números da coluna 2 é {somacoluna2}')
print(f'A soma dos números da coluna 3 é {somacoluna3}')