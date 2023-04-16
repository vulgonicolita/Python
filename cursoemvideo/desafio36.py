a = float(input("\033[1;32mInforme o primeiro comprimento de uma reta: "))
b = float(input("\033[1;32mInforme o segundo comprimento de uma reta: "))
c = float(input("\033[1;32mInforme o terceiro comprimento de uma reta: "))
if a+b > c and a+c > b and b+c > a:
    print("\033[1;34mPode formar um triângulo!")
else:
    print("\033[1;31mNão pode formar um triângulo!")