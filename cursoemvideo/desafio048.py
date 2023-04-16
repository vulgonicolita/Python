soma = 0 #acumulador
contador = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c
        contador += 1
print("A quantidade de números é de {} e a soma de todos eles é {}".format(contador,soma))