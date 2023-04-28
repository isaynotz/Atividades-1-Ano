#53 - Crie um programa que crie uma matriz de dimensão 6x6 e preencha com valores lidos pelo teclado.
#A - Mostre a matriz na tela, com a formatação correta.
#B - Mostre a soma de todos os números pares digitados.
#C - Mostre a soma dos valores da quinta coluna.
#D - Mostre a soma dos valores da sexta linha.
#E - O maior valor da primeira coluna.

matriz =[[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]

somapar = somacoluna5 = somalinha6 = maior = 0

for linha in range(0,6):
    for coluna in range(0,6):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha},{coluna}]: '))
print('-='*30)

for linha in range(0,6):
    for coluna in range(0,6):
        if matriz[linha][coluna] %2 == 0:
            somapar += matriz[linha][coluna]
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print('')
print('=-'*30)
print(f'A soma dos números pares é {somapar}')

for linha in range(0,6):
    somacoluna5 += matriz[linha][4]
    if matriz[linha][0] > maior:
        maior = matriz[linha][0]

for coluna in range(0,6):
    somalinha6 += matriz[5][coluna]

print(f'A soma dos números da quinta coluna é {somacoluna5}')
print(f'A soma dos números da sexta linha é {somalinha6}')
print(f'O maior valor da primeira coluna é {maior}')