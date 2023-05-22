n1 = int(input('Quantos dias o carro foi alugado? '))
n2 = float(input('Quantos Km rodados? '))
valor = (n1 * 60) + (0.15 * n2)
print('Você alugou por {} dias e percorreu {}Km, logo o valor do aluguel do carro foi R${:.2f} '.format(n1, n2, valor))
