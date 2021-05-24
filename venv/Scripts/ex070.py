total = 0
quantidade = 0
barato = ''
valor = 0
while True:
    produto = input('Qual o nome do produto? ')
    valor_anterior = valor
    valor = float(input('Qual o preço do produto? '))
    total += valor
    if valor > 1000:
        quantidade += 1
    if valor < valor_anterior:
        barato = produto
    c = input('Deseja continuar? [S/N] ').strip().lower()
    if c in 'n':
        print(f'o valor total gasto na compra é de R${total:.2f} \n{quantidade} produtos custaram mais de R$1000,00 '
              f'\nO produto mais barato foi {barato}')
        break
