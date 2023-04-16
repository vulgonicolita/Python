notas = []
s = 0
for c in range(1,5):
    nota = float(input('Digite a {} nota: '.format(c)))
    notas.append(nota)
    s += nota
    media = s/4
print('As notas do aluno são: {} e a sua média é {}'.format(notas, media))
