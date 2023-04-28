c = int(input('Digite o código do operário: '))
n = int(input('Digite o número de horas trabalhadas do operário: '))
he = n - 50
e = he * 20
s = n * 10

if n > 50:
    s = e + 500
    print('O salário do operário é R${}. Extra: R${}.'.format(s,e))
else:
    e = 0
    print('O salário do operário é R${}.'.format(s))