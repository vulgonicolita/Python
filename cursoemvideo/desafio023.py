n1 = int(input("Digite um número de 0 a 9999: "))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print("A sua unidade é {}".format(u))
print("A sua dezena é {}".format(d))
print("A sua centena é {}".format(c))
print("o su milhar é {}".format(m))