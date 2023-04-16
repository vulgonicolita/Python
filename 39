frase = str(input("Digite aqui uma frase: ")).strip().upper()
separado = frase.split() #separar as palavras
junto = "".join(separado)
inverso = "" #variavel vazia para nao add nada, não pode botar um número
print(junto)
for c in range(len(junto) -1,-1,-1): #se a frase tem 10 letras, ele vai contar do 0 ao nove, por isso bota o primeiro -1 para poder contar do 0 ao 10
    inverso+= junto[c] #a variavel inverso(que esta vazia que é igual ela mesmo + o junto na listagem de c)
#o if e else pode sair do for porque ja criamos uma nova variavel que vai ter que ser usada
if inverso == junto:
    print("É um palíndrome")
else:
    print("Não é um palíndrome")
