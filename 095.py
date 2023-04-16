idade = []
altura = []
for c in range(1,6):
    idade1 = int(input('Digite a {} idade: '.format(c)))
    idade.append(idade1)
    altura1 = int(input('Digite {} altura: '.format(c)))
    altura.append(altura1)
idade.reverse()
altura.reverse()
print('As idades são: {}\ne as alturas são: {}'.format(idade, altura))
