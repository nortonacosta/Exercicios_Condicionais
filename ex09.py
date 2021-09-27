salario = float(input('Digite seu Salário: '))
prestacao = int(input('Prestação: '))

prestVal = salario / prestacao
print(f'Sua prestação ficara em {prestacao}x de {prestVal}')
if prestVal < salario * 0.2:
    print('Empréstimo Concedido')
else:
    print('Empréstimo não concedido')