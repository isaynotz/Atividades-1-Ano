num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse = True)
num.insert(2, 2)
if 5 in num:
     num.remove(5)
else:
     print(‘Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')



valores = list()
for cont in range(0,5):
      valores.append(int(input('Digite um número: ')))

for c, v in enumerate(valores):
     print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')



a = [2, 3, 4, 7]
# b = a (liga a lista)
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')



teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)



galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')


    
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

#print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[1]} é menor de idade.')
        totmen += 1
    
print(f'Temos {totmai} maiores e {totmen} menores de idade.')



carros = [
    ["Modelo", "HRV"],
    ["Fabricante", "Honda"],
    ["Ano", 2016]
] # Array / List

carros.append(["Cor","Prata"])

#carros[2][1] = 2019
#print(carros[1][1] + '\n')

for l,c in carros:
    print(l + ' | ' + str(c))