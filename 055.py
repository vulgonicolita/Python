A = 80000
B = 200000
TA = 0.03
TB = 0.015
anos = 0
while A < B:
    A = A + (A * TA)
    B = B + (B * TB)
    anos = anos + 1
print("A população A ultrapassará a população B em {} anos".format(anos))
