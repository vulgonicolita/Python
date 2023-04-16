materia = str(input("Digite o nome da matéria: "))
materia1 = materia.capitalize()
nome = str(input("Digite o nome do aluno: "))
nome1 = nome.capitalize()
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2
print("="*30)
print("O nome da matéria é {}".format(materia1))
print("="*30)
print("O nome do aluno é {}".format(nome1))
print("="*30)
if media >= 0 and media < 4:
    print("Sua média E")
elif media >= 4 and media < 6:
    print("Sua média D")
elif media >= 6 and media < 7.5:
    print("Sua média C")
elif media >= 7.5 and media < 9:
    print("Sua média B")
elif media >= 9 and media == 10:
    print("Sua média A")