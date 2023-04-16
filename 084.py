num = []
pares = []
impares = []
for c in range(1,21):
    numeros = int(input('Digite {} número inteiro: '.format(c)))
    num.append(numeros)
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)
print('Os número inseridos são: {}\nOs pares são: {}\nOs ímpares são: {}'.format(num, pares, impares))
