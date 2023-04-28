

#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = str
print('[M] - Masculino \n[F] - Feminino')

while s == str:
    n = str(input('Digite seu sexo: ')).upper()
    if n == 'M' or n == 'F':
        print('Sexo computado com sucesso.')
    else:
        print('Tente novamente.')


# In[14]:


#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] - Somar
#[2] - Multiplicar
#[3] - Subtrair
#[4] - Maior
#[5] - Novos Números
#[6] - Sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso

v1 = v2 = 0
opcao = 0

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

while opcao != 6:
    print('Menu: \n[1] - Somar \n[2] - Multiplicar \n[3] - Subtrair \n[4] - Maior \n[5] - Novos Números \n[6] - Sair do programa\n')
    opcao = int(input('Digite a opção desejada: '))
    
    if opcao == 1:
        print('''Somar''')
        soma = v1 + v2
        print('O valor da soma é: {}\n'.format(soma))
        
    elif opcao == 2:
        print ('''Multiplicar''')
        multiplicar = v1 * v2
        print('O valor da multiplicação é {}\n'.format(multiplicar))
        
    elif opcao == 3:
        print('''Subtrair''')
        subtracao = v1 - v2
        print('O valor da subtração é {}\n'.format(subtracao))
    
    elif opcao == 4:
        print('''Maior''')
        if v1 > v2:
            print('O maior número é {}'.format(v1))
        else:
            print('O maior número é {}'.format(v2))
    
    elif opcao == 5:
        v1 = float(input('Digite o novo valor: '))
        v2 = float(input('Digite o novo segundo valor: '))
    
    elif opcao == 6:
        print('Programa interrompido.')
    
    else:
        print('Opção inválida, tente novamente.')


# In[3]:


# Faça um programa que leia um número qualquer e mostre o sue fatorial. Utilize o while para realizar
# esse exercício.

cont = f = 1
n = int(input('Digite um número inteiro para mostrar seu fatorial: '))
while cont <= n:
    f = cont * f
    cont = cont + 1
print('O fatorial do número {} é {}'.format(n,f))


# In[4]:


#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
#usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados
#e qual foi a soma entre eles

s = n = 0

while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        s = n + s
    else:
        continue

print(s)


# In[7]:


#Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre a média
#entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se
#ele quer ou não continuar a digitar valores.

menor = 99999
qn = sn = maior = 0
op = 'S'

while op == 'S':
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    else:
        menor = n
    qn = qn + 1
    sn = sn + n
    op = str(input('Deseja continuar? [S/N]: ')).upper()

mn = sn/qn

print('A média dos números é: {} \nO maior número é {} \nO menor número é {}'.format(mn,maior,menor))
    


# In[9]:


# Desenvolva um programa que calcule a tabuada de um número qualquer. Utilize o while para desenvovler esse exercício.

cont = 1
t = 0

n = int(input('Digite um número para saber a tabuada dele: '))

while cont <= 10:
    t = n * cont
    print('{} x {} = {}'.format(n,cont,t))
    cont += 1


# In[4]:


# Em uma empresa de qualquer, trabalha vários funcionários. Calcule a média de idade
# de homens e mulheres. Qual a maior idade e qual a menor idade de homens e mulheres.
# O programa deverá solicitar se deseja continuar ou não a execução do programa.

idadef = idadem = maiorm = maiorf = mediaidm = mediaidf = qm = qf = 0
menorm = menorf = 99999
op = 'S'

while op == 'S':
    print('Empresa: \n')
    sex = str(input('Qual o gênero do empregado? [M/F]: ')).upper()
    
    if sex == 'F':
        qf += 1
        idf = int(input('Digite a idade do empregado: '))
        if idf > 0:
            idadef += idf
            if idf > maiorf:
                maiorf = idf
            else:
                menorf = idf
        else:
            continue
    
    elif sex == 'M':
        qm += 1
        idm = int(input('Digite a idade do empregado: '))
        if idm > 0:
            idadem += idm
            if idm > maiorm:
                maiorm = idm
            else:
                menorm = idm
        else:
            continue
    
    else:
        print('Tente novamente.')
        
    op = str(input('Deseja continuar? [S/N]: ')).upper()

mediaidm = idm/qm
mediaidf = idf/qf

print('A média de idade dos homens é {} \nA média de idade das mulheres é {}\n'.format(mediaidm, mediaidf))
print('Maior idade dos homens é {} \nMenor idade dos homens é {} \nMaior idade das mulheres é {} \nMenor idade das mulheres é {}'.format(maiorm,menorm,maiorf,menorf))

# In[ ]:

#Desenvolva um programa que calcule o vencedor de uma eleição de uma cidade.
#Candidatos:
#10 - Pernalonga
#30 - Frajola
#42 - Taz
#55 - Patolino
#01 - Branco
#00 - Sair da Eleição
#Sabendo que qualquer número diferente desse, é voto nulo.
#Qual candidato venceu a eleição?
#O candidato que teve mais votos, ganhou com quantos?
#Qual a média de votos de cada candidato?
#Qual a porcentagem de votos de cada candidato?

qvpe=qvf=qvt=qvpa=qvb=qvn=tv=0
voto=0
print('Escolha seu candidato: Pernalonga - 10 \n30 - Frajola \n42 - Taz \n55 - Patolino')

voto= int(input('Digite o seu voto: '))

while voto != 00:
    voto= int(input('Digite o seu voto: '))
    if voto==10:
        qvpe += 1
    if voto==30:
        qvf += 1
    if voto==42:
        qvt += 1
    if voto==55:
        qvpa += 1
    if voto==1:
        qvb += 1
    else:
        qvn += 1
        
tv = qvpe+qvf+qvt+qvpa

ppe = (qvpe*100)/tv
pf = (qvf*100)/tv
pt = (qvt*100)/tv
ppa = (qvpa*100)/tv

mpe = qvpe/4
mf = qvf/4
mt = qvt/4
mpa = qvpa/4

if qvpe>qvf and qvpe>qvt and qvpe>qvpa:
    vencedor='Pernalonga'
    qv=qvpe
elif qvf>qvpe and qvf>qvt and qvf>qvpa:
    vencedor='Frajola'
    qv=qvf
elif qvt>qvpe and qvt>qvf and qvt>qvpa:
    vencedor='Taz'
    qv=qvt
elif qvpa>qvpe and qvpa>qvt and qvpa>qvf:
    vencedor='Patolino'
    qv=qvpa

print('O vencedor da eleição é o candidato {}, com {} votos\n'.format(vencedor,qv))
print('Quantidade de votos:\n')
print('Pernalonga: {} \nFrajola: {} \nTaz: {} \nPatolino: {}\n'.format(mpe,mf,mt,mpa))
print('Pernalonga: {}% \nFrajola: {}% \nTaz: {}% \nPatolino: {}%\n'.format(ppe,pf,pt,ppa))

#Desenvolva  um programa que calcule a quantidade de homens e mulheres de uma empresa .
#Diante deisso calcule:
#A quantidade de homens e mulheres desta empresa.
#A média de homens e mulheres que trabalham nesta empresa.

op = 'S'
qm = qf = qt = 0

while op == 'S':
    print('Empresa:')
    sex = str(input('Qual o gênero da pessoa? [M/F]: ')).upper()
    
    if sex == 'M':
        qt += 1
        qm += 1
        
    elif sex == 'F':
        qt += 1
        qf += 1
        
    else:
        print('Tente novamente.')
    
    op = str(input('Deseja continuar? [S/N]: ')).upper()

mm = qm/qt
mf = qf/qt

print('Quantidade de homens na empresa: {} \nQuantidade de mulheres na empresa: {}\n'.format(qm,qf))
print('Média de homens na empresa: {} \nMédia de mulheres na empresa: {}\n'.format(mm,mf))

#Desenvolva um programa que calcule o peso e a idade de várias pessoas na cidade.
#Sabendo disso mostre:
#Maior Peso
#Menor Peso
#Média das idades.

op = 'S'
maiorp = idadet = qp = 0
menorp = 99999

while op = 'S':
    peso = float(input('Digite o seu peso: '))
    if peso > 0:
        qp += 1
        if peso > maiorp:
            maiorp = peso
        else:
            menorp = peso
        idade = int(input('Digite a sua idade: '))
        if idade > 0:
            idadet += idade
        else:
            qp = qp - 1
    
    op = str(input('Deseja continuar? [S/N]: ')).upper()
    
mi = idadet/qp

print('Maior peso: {} \nMenor peso: {}\n'.format(m))
print('Média das idades: {}'.format(mi))

#Desenvolva um programa que calcule a quantidade de pessoas que compraram ingresso para uma sessão de
#cinema. Sabendo que:
#Sala 1 - Thor: Amor e Trovão
#Sala 2 - Avengers
#Sala 3 - O outro Eu
#Sala 4 - Minions 2
#Diferente disso, o programa deverá sair.
#Com essas informações calcule a quantidade de pessoas que irão assistir aos filmes em cada sala.
#Media GERAL de pessoas que frequentaram o cinema naquele momento.
#Porcentagem de pessoas em cada sala.

f = 1
sala1 = sala2 = sala3 = sala4 = qg = 0
print('Salas: \nSala 1 - Thor: Amor e Trovão \nSala 2 - Avengers \nSala 3 - O outro Eu \nSala 4 - Minions 2'))
    
while f<=4 and f>=1:
    f= int(input('Digite a sala do filme que assistiu: '))
    if f == 1:
        s1 += 1
        qp += 1
        
    elif f == 2:
        s2 += 1
        qp += 1
        
    elif f == 3:
        s3 += 1
        qp += 1
        
    elif f ==4:
        s4 += 1
        qp += 1

qs1= (sala1*100)/qp
qs2= (sala2*100)/qp
qs3= (sala3*100)/qp
qs4= (sala4*100)/qp

mg= qp/4 

print('Quantidde de pessoas que vão assistir aos filmes: \nSala 1: {} \nSala 2: {} \nSala 3: {} \nSala 4: {}\n'.format(s1,s2,s3,s4))
print('Média geral de pessoas que frequentaram o cinema: \nMédia: {}'.format(mg))

print('Sala 1: {} \nSala 2: {} \nSala 3: {} \nSala 4: {}'.format(qs1,qs2,qs3,qs4))



