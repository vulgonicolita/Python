from datetime import date
contmaior = 0
contmenor = 0
for c in range(1,8):#numerar as pessoas
    ano = int(input("Digite o ano de seu nascimento: "))
    maior = date.today().year - ano #importei uma biblioteca que me diz o ano atual e aqui vamso descobrir a idade
    print("A pessoa {} tem {} anos".format(c,maior)) #a cada pessoa que digitar seu ano, vai aparecer sua idade
    if maior >= 18: #Se a idade for maior que 18 vai contar uma pessoa
        contmaior+=1
    else: #Se a idade for menor que 18 vai contar uma pessoa
        contmenor+=1
print("{} pessoas atingiram a maioridade".format(contmaior)) #Mostra o total de pessoas que atingiram a maioridade
print("{} pessoas não atingiram a maioridade".format(contmenor)) #Mostra o total de pessoas que não atingiram a maioridade
