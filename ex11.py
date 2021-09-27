n = int(input('DIgite um número maior que zero: '))
soma = 0
if n > 0:

    num = str(n)
    for i in range(len(num)):
        soma += int(num[i])
    print(f'A soma é de: {soma}')
else:
    print('Número inválido....Encerrando....')
