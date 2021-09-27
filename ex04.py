import math

n = int(input('Digite um número: '))
if n > 0:
    print(f'O número {n} ao quadrado é: {n ** 2}')
    print(f'A raiz quadrada de {n} é: {math.sqrt(n)}')
else:
    print('Número inválido')

