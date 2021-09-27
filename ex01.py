n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 == n2:
    print(f'Os valores digitados são iguais.')
elif n1 > n2:
    print(f'O valor {n1} é maior que o valor {n2}')
elif n2 > n1:
    print(f'O valor {n2} é maior que {n1}')