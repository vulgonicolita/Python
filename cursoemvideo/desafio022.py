nome = str(input("Digite o seu nome completo: ")).strip()
print("Analisando o seu nome completo...")
print("O seu nome em maiúscula é {}".format(nome.upper()))
print("O seu nome me minúsculo é {}".format(nome.lower()))
print("O seu nome possui {} letras ao todo".format(len(nome)-nome.count(' ')))
nome1 = nome.split()
print("O seu primeiro nome tem {} letras".format(len(nome1[0])))
''' nome1[0] ele esta referindo a primeira palavra da separação.
Observe que quando vem em [] quer dizer que tiroi da lista'''