p1 = float(input("Informe o valor do produto 1: "))
p2 = float(input("Informe o valor do produto 2: "))
p3 = float(input("Informe o valor do produto 3: "))
if p1 < p2 and p1 < p3:
    print("Você deve ter preferência pelo produto 1, pois é mais barato")
elif p2 < p1 and p2 < p3:
    print("Você deve ter preferência pelo produto 2, pois é mais barato")
elif p3 < p1 and p3 < p2:
    print("Você deve ter preferência pelo produto 3, pois é mais barato")
