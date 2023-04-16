h = float(input("Digite a sua altura: "))
i = str(input("Você é homem ou mulher? "))
m = (72.7*h) - 58
f = (62.1*h) - 44.7
if i == "homem":
    print("Seu peso ideal é: ",m,"kg")
else:
    print("Seu peso ideal é ",f,"kg")
