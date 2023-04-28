Algoritmo "Ex6"

Var
na: caracter
pr1,pr2,m:real

Inicio
escreval ("Digite o nome do aluno")
leia(na)
escreval ("Digite a nota da prova 1 do aluno")
leia(pr1)
escreval ("Digite a nota da prova 2 do aluno")
leia(pr2)

m<-(pr1+pr2)/2

escreval ("Nome do aluno : ",na)
escreval ("Nota da prova 1 do aluno : ",pr1)
escreval ("Nota da prova 2 do aluno : ",pr2)

se (m>6.9) entao

   escreval ("Parabéns! Você foi aprovado!")
   
fimse

se (m<3.1) entao

   escreval ("Xiii, você foi reprovado")
   
fimse

se (m>3.1) e (m<7) entao

   escreval ("Você vai para a Prova Final")
   
fimse

Fimalgoritmo