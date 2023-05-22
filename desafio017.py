from math import sqrt

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = sqrt(cateto_oposto**2 + cateto_adjacente**2)

print("O comprimento da hipotenusa é {:.2f}: ".format(hipotenusa))

#cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
#cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
#hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
#print("O comprimento da hipotenusa é {:.2f}: ".format(hipotenusa))

from math import hypot

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print("O comprimento da hipotenusa é {:.2f}: ".format(hipotenusa))
