a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
if a > b and a > c and b > c:
    print("A ordem decrescente é: ",a,b,c)
elif a > c and a > b and c > b:
    print("A ordem decrescente é: ",a,c,b)
elif b > a and b > c and a > c:
    print("A ordem decrescente é: ",b,a,c)
elif b > c and b > a and c > a:
    print("A ordem decrescente é: ",b,c,a)
elif c > a and c > b and a > b:
    print("A ordem decrescente é: ",c,a,b)
elif c > b and c > a and b > a:
    print("A ordem decrescente é: ",c,b,a)
elif a == b and b == c and c == a:
    print("Todos os números são iguais")
