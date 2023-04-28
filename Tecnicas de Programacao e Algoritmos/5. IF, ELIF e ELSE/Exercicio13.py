# Programa Bissexto

ano = int(input('Digite o ano que você deseja saber se é bissexto: '))

if (ano % 4 == 0):
    print('Este ano é bissexto.')
else:
    print('Este ano não é bissexto.')