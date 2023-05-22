n1 = float(input('Seu salário sem aumento: R$'))
a = n1 * 0.15 #ou a + (a * 15/100)
t = a + n1
print('O seu salário com aumento é R${:.2f}.'.format(t))
