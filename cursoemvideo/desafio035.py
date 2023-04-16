salario = float(input("Informe o seu salário: "))
v1 = salario * (1+0.1)
v2 = salario * (1+0.15)
if salario >= 1200:
    print("O aumento é de 10%. Logo o total vai ser de {} reais".format(v1))
else:
    print("O aumento é de 15%. Logo o total vai ser de {} reais".format(v2))