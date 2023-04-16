v = float(input("Digite a velocidade do carro: "))
velocidadeacima = v - 80
multa = velocidadeacima * 7
if v <= 80:
    print("Você está no limite!")
else:
    print("Você ultrapassou o limite! Você recebeu uma multa de {} reais".format(multa))