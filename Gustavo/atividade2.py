salario = float(input('Informe seu salário: '))
total, vendas, extra = 0, 0, 0

while True:
    vendas += float(input('Informe o valor da venda: '))
    stop = input('Se não quiser inserir mais vendas informe "stop": ')
    if stop == 'stop':
        break

if vendas <= 1500:
    total = salario + (vendas*0.05)

if vendas > 1500:
    extra = vendas - 1500
    total = salario + ((vendas-extra)*0.05) + ((extra)*0.07)

print(f'O salário final é {total}')
