#52 - Crie um programa que crie uma matriz de dimensão 4x4 e preencha com valores lidos pelo teclado.
#A - Mostre a matriz na tela, com a formatação correta.
#B - Mostre a soma de todos os números ímpares digitados.
#C - Mostre a soma dos valores da terceira coluna.
#D - Mostre a soma de todos os valores da matriz.
#E - O maior valor da quarta coluna.
matriz = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

somaimpar = somatot = somacoluna3 = maior = 0

for linha in range(0,4):
    for coluna in range(0,4):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha},{coluna}]: '))
print('=-'*30)

for linha in range(0,4):
    for coluna in range(0,4):
        somatot += matriz[linha][coluna]
        if matriz[linha][coluna] %2 == 1:
            somaimpar += matriz[linha][coluna]
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()
print('-='*30)
print('')
print(f'A soma dos números ímpares é {somaimpar}')

for linha in range(0,4):
    somacoluna3 += matriz[linha][2]
    if matriz[linha][3] > maior:
        maior = matriz[linha][3]

print(f'A soma dos valores da terceira coluna é {somacoluna3}')
print(f'A soma de todos os valores da matriz é {somatot}')
print(f'O maior valor da quarta coluna é {maior}')
