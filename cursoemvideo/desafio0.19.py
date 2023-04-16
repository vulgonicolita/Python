import random
n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do quarto aluno: "))
n4 = str(input("Digite o nome do quinto aluno: "))
t = [n1,n2,n3,n4]
print("Os nomes que você escolheu foi {}".format(t))
print("O nome sorteado é {}".format(random.choice(t)))