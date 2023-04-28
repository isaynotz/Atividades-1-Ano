# Programa Multa

velo = int(input('Digite a velocidade do carro: '))
velom = velo - 80
multa = velom * 7

if velo > 80:
    print('O valor da sua multa é {}R$.'.format(multa))

else:
    print('Você não foi multado.')