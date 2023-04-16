num = int(input("Digite um número inteiro: "))
print ('''Escolha qual base de conversão você quer:
1 para binário
2 para octal
3 para hexadecimal''')
escolha = int(input("Digite aqui: "))
if escolha == 1:
    print("A conversão para o número binário é de {}".format(bin(num)[2:]))
elif escolha == 2:
    print("A conversão para o número octal é de {}".format(oct(num)[2:]))
elif escolha == 3:
    print("A conversão para o número hexadecimal é de {}".format(hex(num)[2:]))