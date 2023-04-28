t1 = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

n1 = int(input('Digite um número de 0 a 20: '))

if n1 >= 0 and n1 <= 20:
    print('Este número por extenso se escreve: {}'.format(t1[n1]))
else:
    print('Número inválido')