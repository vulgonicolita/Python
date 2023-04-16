num = []
soma = 0
vezes = 1
for c in range(1,6):
    numero = int(input('Digite o {} número: '.format(c)))
    num.append(numero)
    soma += numero
    vezes *= numero
print('Os números que você escolheu foram {}\nA soma entre eles é {}\nA multiplicação é {}'.format(num,soma,vezes))
