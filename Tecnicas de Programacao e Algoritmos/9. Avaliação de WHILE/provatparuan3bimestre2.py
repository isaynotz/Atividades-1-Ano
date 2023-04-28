#EX1

comeco = fim = tab = 1
n = 0

n = int(input('Digite um número que você deseja saber a tabuada: '))
comeco = int(input('Começar a tabuada em: '))
fim = int(input('Terminar em: '))
if fim < comeco:
    print('Fim maior que o começo, tente novamente.')
    comeco = int(input('Começar a tabuada em: '))
    fim = int(input('Terminar em: '))
else:
    while comeco <= fim:
        tab = n * comeco
        print ('{} x {} = {}'.format(n,comeco,tab))
        comeco += 1
    print('Fim da execução')

#EX2

cont = 0
pfinal = 0
ppao = float(input('Digite o preço do pão: '))

print('''      Preço do pão: R$ {}
    Panificadora Pão de Ontem   '''.format(ppao))
print('')
while cont < 50:
    pfinal += ppao
    cont += 1
    print('{} - R${}'.format(cont,pfinal))
print('Fim dos preços.')

#EX3

preco = cont = sp = 1
tot = 0

while sp == 1:
    preco = float(input('Digite o preço do produto'))
    
    if preco > 0:
        tot += preco
        print('Produto {}: R${}'.format(cont,preco))
        cont += 1
    else:
        print('Total: R${}'.format(tot))
        din = float(input('Valor em dinheiro para pagar: R$'))
        troco = din - tot
        if din < tot:
            print('Quantia de dinheiro menor que o total da compra, tente novamente.')
            continue
        else:
            print('Dinheiro: R${} \nTroco: R${}'.format(din,troco))
            tot = 0


