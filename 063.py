num = 1 #variavel num recebe um valor diferente de 0 de preferencia 1, pois vamos somá-los depois
soma = 0
cont = 0
while num != 0: #enquanto numero for diferente de 0 a gente imprime esse valor
    num = int(input("Digite um valor: "))
    soma += num #somar os números
    cont += 1 #contabilizar quantos números entraram na conta
media = (soma)/(cont-1) #tirei 1 para desconsiderar o 0 na divisão
print("A soma dos números é {}\nA quantidade de números digitados, desconsiderando o 0 foi {}\nSua média é {}".format(soma,cont-1,media))
