a = float(input("\033[1;32mInforme o primeiro comprimento de uma reta: "))
b = float(input("\033[1;32mInforme o segundo comprimento de uma reta: "))
c = float(input("\033[1;32mInforme o terceiro comprimento de uma reta: "))
if a+b > c and a+c > b and b+c > a and a == b and b == c:
    print("\033[1;34mPode formar um triângulo!")
    print("\033[1;36mO triângulo é equilatero")
elif a+b > c and a+c > b and b+c > a and a == b and a != c:
    print("\033[1;34mPode formar um triângulo!")
    print("\033[1;36mO triângulo é isóceles")
elif a+b > c and a+c > b and b+c > a and a == c and a != b:
    print("\033[1;34mPode formar um triângulo!")
    print("\033[1;36mO triângulo é isóceles")
elif a+b > c and a+c > b and b+c > a and b == c and b != a:
    print("\033[1;34mPode formar um triângulo!")
    print("\033[1;36mO triângulo é isóceles")
elif a+b > c and a+c > b and b+c > a and a != b and a != c and b != c:
    print("\033[1;34mPode formar um triângulo!")
    print("\033[1;36mO triângulo escaleno")
else:
    print("\033[1;31mNão pode formar um triângulo!")y
