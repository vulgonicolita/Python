nome = str(input("Digite seu nome de usuário: "))
senha = str(input("Digite sua senha: "))
while nome == senha: #enquanto nome e senha forem iguais ele vai pedir uma nova senha e um novo nome de usuario
    print("O nome de usuário e senha não podem ser iguais!")
    nome = str(input("Digite seu nome de usuário: "))
    senha = str(input("Digite sua senha: "))
print("Foi aceito o nome de usuário e a senha!")