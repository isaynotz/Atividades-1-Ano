#Programa Alistamento

ano = int(input('Digite o ano em que você nasceu: '))
anor = 2022 - ano
anoresto = anor - 18

if 2022 - ano == 18:
    print('Você está pronto para se alistar, vá já se alistar!!')

elif 2022 - ano > 18:
    print('Você está pronto para se alistar, e já passou {} anos do tempo certo para se alistar.'.format(anoresto))

else:
    print('Você não está pronto para se alistar.')