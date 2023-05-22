from math import trunc
num = float(input('Digite um valor: '))
print('O número digitado arredondado foi {}'.format(trunc(num)))

#ou poderia usar
#num - float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))