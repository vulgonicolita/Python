frase = str(input("Digite uma frase qualquer: ")).strip()
print("Analisando sua frase...")
frase1 = frase.lower()
frase2 = frase1.count('a')
frase3 = frase1.find('a')+1
frase4 = frase1.rfind('a')+1
print("Sua frase possui {} 'a'".format(frase2))
print("O primeiro 'a' apareceu na poisção {}".format(frase3))
print("A ultima vez que apareceu o 'a' foi na posição {}".format(frase4))
