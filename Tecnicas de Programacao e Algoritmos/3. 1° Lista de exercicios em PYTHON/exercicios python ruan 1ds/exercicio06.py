#Programa Dólar

dolar=float(input('Digite a cotação atual do dólar: '))
real=float(input('Digite quantos reais você possui em sua carteira: '))
conv=real/dolar

print(input('Em dólares você possui {}$'.format(conv)))