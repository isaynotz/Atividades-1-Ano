#!/usr/bin/env python
# coding: utf-8

# In[42]:


lista = []
for cont in range(0,5):
    lista.append(int(input('Digite um número: ')))

print(f'Números digitados: {len(lista)}')
print(f'Ordem decrescente: {sorted(lista, reverse = True)}')
if 5 in lista:
    print(f'Posição do número cinco: {lista.index(5)+1}° número digitado')
else:
    print('O número 5 não foi digitado.')


# In[47]:


times = ('Palmeiras','Internacional','Flamengo','Fluminense','Corinthians','Athletico-PR','Atlético-MG','América-MG','Fortaleza','São Paulo','Botafogo','Santos','Bragantino','Goiás','Coritiba','Ceará','Cuiabá','Atlético-GO','Avaí','Juventude')

print(f'Os 5 primeiros colocados: {times[0:5]}')
print(f'Os últimos 4 colocados: {times[16:20]}')
print(f'Ordem alfabética: \n{sorted(times)}')
print('Posição do time Juventude: {}°'.format(times.index('Juventude')+1))


# In[49]:


tupla = (int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')))

print(f'Quantidade de vezes que o número 9 aparece: {tupla.count(9)}')
if 3 in tupla:
    print(f'O número 3 apareceu na posição: {tupla.index(3)}°')
else:
    print('O número 3 não apareceu na tupla')
print('Números pares: \n',end='')
for n in tupla:
    if n%2 == 0:
        print(n)


# In[29]:


produto = (('KG Pão', 5),('Teclado', 70),('Papel Higiênico', 7),('Manga', 5),('Leite',7))
print('{:<20} {:<15}'.format('Produto','Preço'))
for cont in produto:
    produto, preco = cont
    print('{:<20} {:<15}'.format(produto,preco))


# In[ ]:


palavras = ('Manga', 'Pao', 'Livro', 'Quimica', 'Produto', 'Time')

for n in palavras:
    print(f'\nNa palavra {n} tem as vogais:', end = '')
    for v in n:
        if v.lower() in 'aeiou':
            print(v, end ='')

