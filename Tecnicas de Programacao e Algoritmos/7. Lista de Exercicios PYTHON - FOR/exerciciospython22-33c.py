#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Ex22

#Elabore um programa que apresente os números pares de 1 a 100.

s=0

for cont in range(1,101):
    if cont%2==0:
        s = s + 1
    
print(s)


# In[ ]:

# Ex23

# Desenvolva um programa que leia 50 números inteiros, conte quantos são divisíveis por 3 e exiba o resultado.

s=0

for cont in range(0,50):

    n = int(input('Digite um número: '))
    if n%3==0:
        s= s +1
print('A quantidade de números divisíveis por 3 é: {}.'.format(s))


# In[ ]:

# Ex24

#Desenvolva um programa que leia 40 números reais,
#somar e calcular a média dos números positivos
#e contar os números negativos e exiba os resultados.

sp=qp=sn=qn= 0

for cont in range(1, 41, 1): 
    n = float(input('Digite um número: '))
    if n>0: 
        sp = n + sp
        qp = qp + 1
    else:
        sn = n + sn
        qn = qn + 1

if qp == 0:
    print('Tente novamente.')
else:
    mp= sp/qp
    print('A média dos números positívos é {}.'.format(mp))
    print('A quantidade dos números positívos é {}.'.format(qp))
    print('A quantidade dos números negativos é {}'.format(qn))

# In[26]:

# Ex25

#Desenvolva um programa que leia o nome
#e a idade de 20 pessoas,
#calcule e exiba a média das idades.

si = 0

for cont in range(1, 21, 1):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    si = idade + si
    
mi = si/20
print('A média de idade dessas pessoas é: {}.'.format(mi))


# In[41]:

#Ex26

#Desenvolva um programa que leia o sexo (Masculino / Feminino) e o salário de 15 pessoas,
#calcule e exiba a média dos salários dos homens e das mulheres.

qm = qf = sm = sf = 0

print('1 - Masculino \n2- Feminino')
for cont in range(1,16,1):
    s = int(input('Digite seu gênero: '))
    if s == 1:
        qm = qm + 1
        salm = float(input('Digite seu salário: '))
        sm = sm + salm
    elif s == 2:
        qf = qf + 1
        salf = float(input('Digite seu salário: '))
        sf = sf + salf
    else:
        print('Opção inválida.')
    
mm = sm/qm
mf = sf/qf

print('A média do salário dos homens é: R${}. \nA média do salário das mulheres é R${}.'.format(mm,mf))


# In[42]:

#Ex27

#Crie um programa que calcule a soma entre todos os números ímpares que são múltiplos
#de três e que se encontram no intervalo de 1 até 500.

s=qi=0
for cont in range(1,501,1):
    if cont%2==1 and cont%3==0:
        qi=qi+1
        s=cont+s
print('A quantidade de números ímpares é de {} \ne a soma dos números ímpares múltiplos de três é: {}'.format(qi,s))


# In[ ]:

#Ex28

#Desenvolva um programa que leia o primeiro termo e
#a razão de uma PA (Progressão Aritmética). No final, mostre os 10 primeiros termos dessa progressão.

ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = ptermo + (10-1) * razao

for cont in range (ptermo, decimo+razao, razao):
    print(cont)
print('ACABOU')


#Ex29

#Um total de 500 alunos de uma universidade foram entrevistados. De cada um deles foram colhidas as seguintes informações:
#o código do curso que frequenta (1-engenharia; 2-computação; 3-administração) e a idade. Desenvolva um programa que processe
# estes dados e que forneça as seguintes informações:
# • número de alunos por curso;
# • número de alunos com idade entre 20 e 25 anos, por curso; e
# • qual o curso com menor média de idade.

print ('Código do curso: \n1- Engenharia \n2- Computação \n3- Administração')

ie = ic = ia = ne = nc = na = nei = nci = nai = iem = icm = iam = 0

for cont in range(1,501,1):
    curso = int(input('Digite o número do seu curso: '))

    if curso == 1:
        ne = ne + 1
        idade = int(input('Digite a sua idade: '))
        ie = idade + ie
        if idade >= 20 and idade <= 25:
            nei = nei + 1

    elif curso == 2:
        nc = nc + 1
        idade = int(input('Digite a sua idade: '))
        ic = idade + ic
        if idade >= 20 and idade <= 25:
            nci = nci + 1

    elif curso == 3:
        na = na + 1
        idade = int(input('Digite a sua idade: '))
        ia = idade + ia
        if idade >= 20 and idade <= 25:
            nai = nai + 1

    else:
        print('Opção inválida.')

mei = ie/ne
mci = ic/nc
mai = ia/na

print('Número de alunos por curso: \nEngenharia: {}. \nComputação: {}. \nAdministração: {}. \n'.format(ne,nc,na))
print('Número de alunos com idade entre 20 e 25 anos por curso: \nEngenharia: {}. \nComputação: {}. \nAdministração: {}. \n'.format(nei,nci,nai))

if mei < mci and mei < mai:
    print('O curso com menor média de idade é Engenharia, com média de idade de: {}.'.format(mei))
elif mci < mei and mci < mai:
    print('O curso com menor média de idade é Computação, com média de idade de: {}.'.format(mci))
else:
    print('O curso com menor média de idade é Administração, com média de idade de: {}.'.format(mai))

#Ex30

salm = salf = qm = qf = qff = maidm = maidf = 0
meidm = meidf = 99999

n = int(input('Digite a quantidade de habitantes entrevistados: '))
print('------'*8)
print('M - Masculino \nF- Feminino')

for cont in range(1, n+1 ,1):
    sexo = str=input('Digite o gênero do entrevistado: ')
    
    if sexo == 'M' or sexo == 'm':
        qm = qm + 1
        sm = float(input('Digite o salário do entrevistado: '))
        salm = sm + salm
        
        idadem = int(input('Digite a idade do entrevistado: '))
        if idadem < 0:
            print('Não existe idade negativa. \n', end='')
        else:
            if idadem > maidm:
                maidm = idadem
            else:
                meidm = idadem
        
    elif sexo == 'f' or sexo == 'F':
        qf = qf + 1
                     
        idadef = int(input('Digite a idade do entrevistado: '))
            
        if idadef < 0:
            print(end='')
        else:
            if idadef > maidf:
                maidf = idadef
            else:
                meidf = idadef
        
        sf = float(input('Digite o salário do entrevistado: '))
            
        if sf <= 1000:
            qff = qff + 1
            salf = sm + salf
        else:
            salf + sm + salf
    
    else:
        print('Opção inválida! Tente novamente.')
            
msm = salm / qm
msf = salf / qf

print('Média salário masculino: {} \nMédia salário feminino: {}'.format(msm, msf))
print('Maior idade masculina: {} \nMenor idade masculina: {}'.format(maidm, meidm))
print('Maior idade feminina: {} \nMenor idade feminina: {}'.format(maidf, meidf))
print('Quantidade de mulheres com salário até R$1000,00: {}'.format(qff))

#Ex 31

# Num frigorifico existem 90 bois. Cada boi traz em su pescoço um cartão contendo um número de identificação e seu
# peso. Escrever um algoritmo que leia o cartão e o peso dos 90 bois e ao final imprima o número e o peso do boi
# mais gordo e do boi mais magro.

maior = idma = idme = 0
menor = 99999

for cont in range(1,91,1):
    id = int(input('Digite o número de identificação do boi: '))
    peso = float(input('Digite o peso do boi: '))
    
    if peso > maior:
        maior = peso
        idma = id
    else:
        menor = peso
        idme = id
print('O boi mais gordo de número de identificação {} pesa {}kg, e o boi mais magro de número de identificação {} pesa {}kg.'.format(idma,maior,idme,menor))

#Ex32

#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite o número: '))
tot = 0

for cont in range(1, num+1, 1):
    if num % cont == 0:
        print('\033[33m',end='  ')
        tot = tot + 1

    else:
        print('\033[31m',end='  ')
    
    print('{}'.format(cont),end=' ➜')

print('\n\o33[m O número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('O número {} é um número primo!!'.format(num))
    
else:
    print('O número {} não é um número primo!!'.format(num))

#Ex33

# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantos já são maiores de idade.

qpma = qpme = 0

anoatual = int(input('Digite o ano atual: '))

for cont in range(1, 5, 1):
    anops = int(input('Digite o ano em que você nasceu: '))
    
    if anops <= anoatual and anoatual - anops >= 18:
        qpma = qpma + 1
    elif anops <= anoatual and anoatual - anops < 18:
        qpme = qpme + 1
    else:
        print('Ano maior que 2022, tente novamente')
print('Quantidade de pessoas maior de idade {}. \nQuantidade de pessoas menor de idade {}.'.format(qpma,qpme))