n = int(input("Digite um número inteiro: "))
p = n%2
if p == 0:
    print("\033[0;33mO número que você escolheu é par.")
else:
    print("\033[0;33mO número que você escolheu é impar.")
