# Programa KM

km = float(input('Digite a distãncia da sua viagem em km: '))
km1 = km * 0.5
km2 = km * 0.45

if km <= 200:

    print('O valor da sua viagem é {}R$.'.format(km1))

else:

    print('O valor da sua viagem é {}R$.'.format(km2))