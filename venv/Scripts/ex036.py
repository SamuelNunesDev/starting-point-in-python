c = float(input('Qual o valor da casa?'))
s = float(input('Qual o salário do comprador?'))
t = float(input('Em quantos anos ele irá pagar?'))
tm = t * 12
p = c / tm
porcentagem = s * 30 / 100
if porcentagem > p:
	print('Empréstimo negado!')
else:
	print(f'Empréstimo aprovado! O valor de cada parcela será de R${p:.2f}')
