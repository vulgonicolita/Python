primeiro = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite aqui a razão da PA: "))
for c in range(1,11):
    print("{}".format(primeiro+(c-1)*razão),end=", ") #Fórmula da razão
print("Acabou.")