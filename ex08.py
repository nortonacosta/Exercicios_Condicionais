n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

if 0.00 <= n1 <= 10 and 0.00 <= n2 <= 10:
    media = (n1 + n2) / 2
    print(f'Média: {media:.2f}')
else:
    print('Nota não informada corretamente (Nota 0.00 à 10)')


