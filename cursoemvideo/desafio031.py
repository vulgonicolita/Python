distancia = float(input("\033[1;31mDigite a distância da viagem em km: "))
v1 = distancia * 0.5
v2 = distancia * 0.45
if distancia <= 200:
    print("\033[1;36mO preço da passagem é de {} reais".format(v1))
else:
    print("\033[1;33mO preço da passagem é de {} reais".format(v2))