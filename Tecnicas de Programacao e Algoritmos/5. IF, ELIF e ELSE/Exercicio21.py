# Criar um game de Pedra, Papel e Tesoura


from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')

jogador = int(input('Qual a sua jogada? '))

if jogador == 0 or jogador == 1 or jogador == 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')
    sleep(1)

    print('-='*12)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-='*12)

    if computador == 0:
        if jogador == 0:
            print('Empate!!')
        elif jogador == 1:
            print('Vitória de Jogador!!')
        elif jogador == 2:
            print('Derrota :(')
        else:
            print('Jogada inválida.')

    elif computador == 1:
        if jogador == 0:
            print('Derrota :(')
        elif jogador == 1:
            print('Empate!!')
        elif jogador == 2:
            print('Vitória de Jogador!!')
        else:
            print('Jogada inválida.')

    elif computador == 2:
        if jogador == 0:
            print('Vitória de Jogador!!')
        elif jogador == 1:
            print('Derrota :(')
        elif jogador == 2:
            print('Empate!!')
        else:
            print('Jogada inválida.')

else:
    print('Opção inválida!! Tente novamente.')
