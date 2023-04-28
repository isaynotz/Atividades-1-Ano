print('.......Desconto do INSS....... \n ')
print('''Desconto
Menor ou igual a R$600,00      Isento
Maior que R$600,00 e menor ou igual a R$1200,00      20%
Maior que R$1200,00 e menor ou igual a R$2000,00      25%
Maior que R$2000,00      30%
''')

s = float(input('Digite o seu salário: '))

if s <= 600:
    print('Você está livre de descontos.')
elif s > 600 and s <= 1200:
    d = s * 0.2
    print('Seu salário de R${} terá um desconto de R${}.'.format(s,d))
elif s > 1200 and s <= 2000:
    d = s * 0.25
    print('Seu salário de R${} terá um desconto de R${}.'.format(s,d))
else:
    d = s * 0.3
    print('Seu salário de R${} terá um desconto de R${}.'.format(s,d))