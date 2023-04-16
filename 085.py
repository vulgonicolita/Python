'''Faça um Programa que leia 5 números inteiros e mostre-os. Usar lista'''
num = []
for c in range (1,6):
    numero = int(input("Digite o {} número: ".format(c)))
    num.append(numero)
print("Os números que você escolheu foram {}".format(num))
