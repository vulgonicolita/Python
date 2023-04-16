x = float(input("Informe quanto você ganha por hora: "))
y = float(input("Informe a quantidade de horas trabalhadas no mês: "))
bruto = x * y
ir = bruto*(1-0.11)
inss = bruto*(1-0.08)
s = bruto*(1-0.05)
tir = bruto - ir
tinss = bruto - inss
ts = bruto - s
liquido = bruto - tir - tinss - ts
print("O salário bruto é de:",bruto)
print("Você pagou {0} de Imposto de Renda, {1} de INSS e {2} de Sindicato".format(tir,tinss,ts))
print("Seu salário líquido é de:",liquido)
