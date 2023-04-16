n = int(input("Digite a quantidade de pessoas na turma: "))
soma = 0
cont = 0
for c in range (1,n+1):
    n1= float(input("Digite a idade do {}º aluno: ".format(c)))
    soma += n1
    cont += 1
    media = soma/cont
if media >= 0 and media <= 25:
    print("A média foi igual {}, logo a turma é jovem!".format(media))
elif media >= 26 and media <= 60:
    print("A média foi igual a {}, logo a turma é adulta!".format(media))
elif media > 60:
    print("A média foi igaul a {}, logo a turma é idosa!".format(media))