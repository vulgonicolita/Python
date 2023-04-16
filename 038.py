num = int(input("Digite um número inteiro: "))
cont = 0
for c in range (1,num+1): #vai fazer a contagem do 1 até o número em que a pessoa botou em cima
    if num % c == 0: #se o número for divisivel pela a sequencia vai mostrar de azul
        print('\033[34m',end= " ")
        cont += 1
    else: #Se ele não for divisível, vai mostrar de preto
        print('\033[m',end= " ")
    print(c,end=" ")#Aqui escreve os números com as cores
#Porém a gente precisa saber quantas vezes o número foi divisivel e para saber a gente cria um contador
#Que inicia a sua contagem do 0 e vai adicionando mais um para toda vez que ele for divisivel
#Se ele for contado duas vezes, o número é primo, caso ao contrário, ele não é primo.
if cont == 2:
    print("\033[m\n Ele é primo")
else:
    print("\033[m\n Ele não é primo")
