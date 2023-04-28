#!/usr/bin/env python
# coding: utf-8

# In[19]:


#1 Desenvolva um porgrama que calcule a tabuada de um número qualquer
#ex
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
#...
# 5 x 10 = 50

n = int(input('Digite o número que você quer saber a tabuada: '))
s = 0
for cont in range(n,n*10+1, n):
    s = s + 1
    print('{} x {} = {}'.format(n,s,cont))


# In[26]:


#2 Em uma empresa de 50 funcionários, calcule a média de idade de homens e mulheres
#Qual a maior idade e qual a menor idade?

idm = idf = qm = qf = 0
maior = 0
menor = 99999

for cont in range(1,51,1):
    print('F - Feminino \nM- Masculino')
    sex = str(input('Digite o seu gênero: '))
    idade = int(input('Digite a sua idade: '))
    
    if idade > maior:
        maior = idade
    else:
        menor = idade
    
    if sex == 'f' or sex == 'F':
        qf = qf + 1
        idf = idade + idf
    elif sex == 'm' or sex == 'M':
        qm = qm + 1
        idm = idade + idm
    else:
        print('Opção inválida, tente novamente.')
        
mf = idf / qf
mm = idm / qm

print('A média de idade feminina é {} anos. \nA média de idade masculina é {} anos.'.format(mf,mm))
print('A maior idade é de {} anos. \nA menor idade é de {} anos.'.format(maior,menor))


# In[ ]:





# In[30]:


#3 - Desenvolva um programa que calcule o vencedor de uma eleição de uma cidade de 50 habitantes.
# Candidatos:
# 10 - Pernalonga
# 30 - Frajola
# 42 - Taz
# 55 - Patolino
# 00 - Branco
# Sabendo que qualquer número diferente desse, é voto nulo.
# Qual candidato venceu a eleição?
# O candidato que teve mais votos, ganhou com quantos?
# Qual a média de votos de cada candidato?
# Qual a porcentagem de votos de cada candidato?

peq = fq = tq = paq = branco = maior = vencedor = qv = vn = 0
menor = 99999

print('.-'*5,'Eleição', '.-'*5)

for cont in range(1, 51, 1):
    print('Candidatos: \n10 - Pernalonga\n30 - Frajola\n42 - Taz\n55 - Patolino\n00 - Branco\n')
    n = int(input('Digite o número do candidato em que você deseja votar: '))
    
    if n == 10:
        qv = qv + 1
        print('Voto computado para o candidato Pernalonga.\n')
        peq = peq + 1
        if peq > maior:
            vencedor = 10
            maior = peq
        else:
            menor = peq
    elif n == 30:
        qv = qv + 1
        print('Voto computado para o candidato Frajola.\n')
        fq = fq + 1
        if fq > maior:
            vencedor = 30
            maior = fq
        else:
            menor = fq
    elif n == 42:
        qv = qv + 1
        print('Voto computado para o candidato Taz.\n')
        tq = tq + 1
        if tq > maior:
            vencedor = 42
            maior = tq
        else:
            menor = tq
    elif n == 55:
        qv = qv + 1
        print('Voto computado para o candidato Patolino.\n')
        paq = paq + 1
        if paq > maior:
            vencedor = 55
            maior = paq
        else:
            menor = paq
    elif n == 1:
        print('O voto foi branco.')
    else:
        vn = vn + 1
        print('O voto foi nulo.')

mpe = peq/qv
mf = fq/qv
mt = tq/qv
mpa = paq/qv
ppe = (peq*100)/qv
pf = (fq*100)/qv
pt = (tq*100)/qv
ppa = (paq*100)/qv

if vencedor == '10':
    print('O candidato Pernalonga ganhou a eleição com {} votos.'.format(maior))
elif vencedor == '30':
    print('O candidato Frajola ganhou a eleição com {} votos.'.format(maior))
elif vencedor == '42':
    print('O candidato Taz ganhou a eleição com {} votos.'.format(maior))
elif vencedor == '55':
    print('O candidato Patolino ganhou a eleição com {} votos.'.format(maior))
else:
    print('Houve um empate.')

print('Média de votos do candidato Pernalonga: {}. \nMédia de votos do candidato Frajola: {}.'.format(mpe,mf))
print('Média de votos do candidato Taz: {}. \nMédia de votos do candidato Patolino: {}.'.format(mt,mpa))
print('Porcentagem de votos de cada candidato: \nPernalonga: {}%.\nFrajola: {}%.\nTaz: {}%. \nPatolino: {}%.'.format(ppe,pf,pt,ppa))
print('Votos nulos: {}'.format())


# In[ ]:




