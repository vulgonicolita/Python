idades = []
alturas = []
for c in range(1,3):
    id = int(input('Digite a idade: '))
    idades.append(id)
    alt = float(input('Digite a altura: '))
    alturas.append(alt)
mediaAltura = sum(alturas)/len(alturas)
qAlunos = 0
for c in range(0,len(idades)):
    if idades[c] > 13 and alturas[c] <= mediaAltura:
        qAlunos += 1
print('O total de alunos com altura menor que a média é de {} alunos'.format(qAlunos))