p = float(input("Digite aqui o preço do produto: "))
print('''Formas de pagamento:
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão''')
formas = int(input("Digite sua opção de pagamento: "))
vista = p * (1-0.1)
cartão = p * (1-0.05)
cartão3 = p * (1+0.2)
if formas == 1:
    print("O valor do produto era de {} reais e vai sair por {} reais.".format(p,vista))
elif formas == 2:
    print("O valor do produto era de {} reais e vai sair por {} reais.".format(p,cartão))
elif formas == 3:
    pa = int(input("Quantas parcelas: "))
    c = p/pa
    print("O produto vai sair de {}x de {} reais ". format(pa,c))
elif formas == 4:
    pa1 = int(input("Quantas parcelas: "))
    c1 = cartão3/pa1
    print("O produto vai sair de {}x de {} reais".format(pa1,c1))