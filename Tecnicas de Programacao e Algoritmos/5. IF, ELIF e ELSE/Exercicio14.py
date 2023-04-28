# Programa Salário

salario = float(input('Digite o salário do seu funcionário: '))
salario10 = (salario * 0.10) + salario
salario15 = (salario * 0.15) + salario

if salario >= 1250.00:
    print('10% de aumento no salário: {}R$.'.format(salario10))
else:
    print('15% de aumento no salário: {}R$.'.format(salario15))