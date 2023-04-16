import random
import time
lista = ("Pedra","Papel","Tesoura")
usuario = str(input("Escolha uma dessas opções: Pedra, Papel ou Tesoura: "))
letras = usuario.capitalize() #deixando a primeira letra em maiúscula
computador = random.choice(lista) #embaralhando a lista
print("="*30)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!")
time.sleep(1)
print("O computador jogou: {}".format(computador))
time.sleep(1)
print("Você jogou: {}".format(letras))
if computador == "Pedra": #computador jogou pedra
    if letras == "Tesoura":
        print("O computador ganhou!")
    elif letras == "Papel":
        print("Você ganhou!")
    elif letras == "Pedra":
        print("Houve um empate")
    else:
        print("Houve um erro!")
elif computador == "Tesoura": #computador jogou tesoura
    if letras == "Tesoura":
        print("Houve um empate!")
    elif letras == "Papel":
        print("O computador ganhou!")
    elif letras == "Pedra":
        print("Você ganhou!")
    else:
        print("Houve um erro!")
elif computador == "Papel": #computador jogou papel
    if letras == "Papel":
        print("Houve um empate!")
    elif letras == "Tesoura":
        print("Você ganhou!")
    elif letras == "Pedra":
        print("O computador ganhou!")
    else:
        print("Houve um erro!")
print("="*30)
