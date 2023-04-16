p = float(input("Informe a quantidade de quilos do peixe: "))
e = p-50
m = e*4
if p > 50:
    print("Você possui em excesso",e,"kg e a multa que você deverá pagar é de R$",m)
else:
    print("Você não precisará pagar multa")