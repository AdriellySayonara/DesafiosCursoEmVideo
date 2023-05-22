n1 = float(input('O preço do produto sem desconto: R$'))
d = (n1 * 0.05)
t = (n1 - d)
print('O valor do produto com desconto de 5% é R${:.2f}'.format(t))