L1 = []
L2 = []
L3 = []
L4 = []
for c in range(0,10):
    num = int(input('Digite um número: '))
    L1.append(num)
for c in range(0,10):
    num = int(input('Digite um número: '))
    L2.append(num)
for c in range(0,10):
    num = int(input('Digite um número: '))
    L3.append(num)
for c in range(0,10):
    L4.append(L1[c])
    L4.append(L2[c])
    L4.append(L3[c])
print('A lista 1: {}\nA lista 2: {}\nA lista 3: {}\nA lista 4: {}'.format(L1,L2,L3,L4))
