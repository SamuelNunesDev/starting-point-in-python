d = int(input('Qual a quantidade de dias alugados? '))
km = float(input('Qual a quantidade de Km rodados? '))
t = d * 60 + km * 0.15
print(f'O valor a pagar pelo aluguem é de R${t:.2f}')
