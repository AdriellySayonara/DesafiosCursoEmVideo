frase = str(input('Digite uma frase: ')).upper().strip()
a = frase.count('A')
inicio = frase.find('A')+1
fim = frase.rfind('A')+1
print('Possui {} letras "a"'.format(a))
print('A letra "a" na frase iniciou na posição {}'.format(inicio))
print('A posição que a letra "a" apareceu a primeira vez foi {}'.format(fim))

