#Programa IMC

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC está no peso ideal.')
elif imc >= 25 and imc <= 30:
    print('Seu IMC está no Sobrepeso.')
elif imc >= 30 and imc <= 40:
    print('Seu IMC está na Obesidade.')
else:
    print('Seu IMC está na Obesidade Mórbida.')