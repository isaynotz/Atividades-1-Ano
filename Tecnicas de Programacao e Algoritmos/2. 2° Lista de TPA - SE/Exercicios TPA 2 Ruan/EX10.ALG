Algoritmo "Ex10"

Var
n1,l30,l45:real

Inicio
escreval ("Digite o valor do seu produto: ")
leia(n1)

l30<- (n1*0.3)+n1
l45<- (n1*0.45)+n1

se (n1<20) entao

    escreval ("Margem de lucro com a taxa de 30%: ",l30, "R$")
    
    senao
    
    escreval ("Margem de lucro com a taxa de 45%: ",l45, "R$")
    
fimse

Fimalgoritmo