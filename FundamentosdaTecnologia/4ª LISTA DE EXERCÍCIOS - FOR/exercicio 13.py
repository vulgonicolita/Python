temperatura = []
for c in range(1,13):
    t = float(input('Digite {} temperatura: '.format(c)))
    temperatura.append(t)
m = sum(temperatura)/len(temperatura)
print(f'Jan: {temperatura[1]}\n'
f'Fev: {temperatura[2]}\n'
f'Mar: {temperatura[3]}\n'
f'Abr: {temperatura[4]}\n'
f'Mai: {temperatura[5]}\n'
f'Jun: {temperatura[6]}\n'
f'Jul: {temperatura[7]}\n'
f'Ago: {temperatura[8]}\n'
f'Set: {temperatura[9]}\n'
f'Out: {temperatura[10]}\n'
f'Nov: {temperatura[11]}\n'
f'Dez: {temperatura[12]}\n'
f'A média de temperaturas anual é {m}')