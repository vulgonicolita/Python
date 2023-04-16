ano = int(input("Informe um ano qualquer: "))
d1 = ano%4
d2 = ano%100
d3 = ano%400
if d1 == 0 and d2 == 0 and d3 == 0:
    print("\033[1;31mO ano que você escolheu é bissexto!")
elif d1 != 0:
    print("\033[1;31mO ano que você escolheu não é bissexto!")
elif d2 != 0:
    print("\033[1;31mO ano que você escolheu é bissexto!")
elif d3 != 0:
    print("\033[1;31mO ano que você escolheu não é bissexto!")
