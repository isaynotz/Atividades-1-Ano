#Programa Natação
#Mirim - 9 anos
#Infantil - 14 anos
#Junior - 19 anos
#Sênior - 25 anos
#Master - Acima de 25 anos

idade = int(input('Digite a sua idade: '))

if idade <= 9:
    print('Sua categoria é Mírim.')

elif idade >= 9 and idade < 14:
    print('Sua categoria é Infantil.')

elif idade >= 14 and idade < 19:
    print('Sua categoria é Junior.')

elif idade >= 19 and idade < 25:
    print('Sua categoria é Sênior.')

else:
    print('Sua categoria é Master.')