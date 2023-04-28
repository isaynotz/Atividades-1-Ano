#Programa Triângulo

l1 = int(input('Insira o lado 1 do seu triangulo: '))
l2 = int(input('Insira o lado 2 do seu triangulo: '))
l3 = int(input('Insira o lado 3 do seu triangulo: '))

if l1 == l2 and l2 == l3:
    print('Todos os lados são iguais, este triângulo é equilátero.')
elif l1 == l2 and l2 != l3 or l1 != l2 and l2 == l3 or l1 == l3 and l2 != l3:
    print('Dois lados são iguais, mas um diferente, este triângulo é isósceles.')
else:
    print('Todos os lados são diferentes, este triângulo é escaleno.')