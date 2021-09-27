h = float(input('Digite sua Altura: '))
sexo = str(input('Sexo (M/F): ')).lower()
if sexo == 'm':
    pIdeal = (72.7 * h) - 58
    print(f'Seu peso ideal é de {pIdeal:.2f}kg')
else:
    pIdeal = (62.1 * h) - 44.7
    print(f'Seu peso ideal é de {pIdeal:.2f}kg')

