import math
op = float(input("Informe o comprimento do cateto oposto: "))
ad = float(input("Informe o comprimento do cateto adjacente: "))
top = math.pow(op,2)
tad = math.pow(ad,2)
hp = top + tad
print("O valor da hipotenusa é de {:.2f}".format(math.sqrt(hp)))