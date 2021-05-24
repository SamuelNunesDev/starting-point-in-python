print('-' * 10, 'Calculadora de Valores', '-' * 10, '\n')
p = float(input('Digite o preço do produto R$'))
print('Escolha a forma de pagamento: \n\n[1] A vista no dinheiro ou cheque. \n[2] A vista no cartão. \n[3] 2x no '
      'cartão. \n[4] 3x ou mais no cartão. \n')
while True:
    o = input('Digite sua opção: ')
    try:
        o = int(o)
        if 1 == o:
            p = p - p * 10 / 100
            print(f'O valor com 10% de desconto será de R${p:.2f}')
            break
        elif 2 == o:
            p = p - p * 5 / 100
            print(f'O valor com 5% de desconto será de R${p:.2f}')
            break
        elif 3 == o:
            print(f'O valor do produto sem acréscimo é de R${p:.2f}')
            break
        elif 4 == o:
            p = p * 20 / 100 + p
            print(f'O valor com 20% de juros é de R${p}')
            break
        else:
            o = print('Digite uma opção válida!')
    except:
        print('Digite uma opção válida!')
