from math import log
n = int(input('Digite um número: '))
if n > 0:
    print(f'O logaritimo de {n} é: {log(n)}')
else:
    print('Número inválido...')