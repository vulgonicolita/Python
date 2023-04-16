casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos = float(input("Quantos anos você irá pagar? "))
prestacao = casa / (anos * 12)
porcentagem = (salario / 100) * 30
if prestacao <= porcentagem:
    print("O empréstimo foi aprovado!")
else:
    print("O empréstimo foi negado!")
