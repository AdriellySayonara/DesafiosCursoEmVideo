import math

angulo = float(input("Digite o valor do ângulo: "))

# Convertendo o ângulo para radianos
angulo_em_radianos = math.radians(angulo)

# Calculando o seno, cosseno e tangente do ângulo
seno = math.sin(angulo_em_radianos)
cosseno = math.cos(angulo_em_radianos)
tangente = math.tan(angulo_em_radianos)

# Imprimindo os resultados na tela
print(f"Seno de {angulo} graus = {seno:.2f}")
print(f"Cosseno de {angulo} graus = {cosseno:.2f}")
print(f"Tangente de {angulo} graus = {tangente:.2f}")
