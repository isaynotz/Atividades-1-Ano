print('''...Regulador de Peso de Peixes...
''')

p = float(input('Digite o peso do seu peixe: '))
e = p - 50

if p > 50:
    m = e * 7
    print('Você pagará R${} de multa por exceder o limite de peso de 50kg.'.format(m))

else:
    print('Peso do peixe de acordo com as normas estabelecidas.')