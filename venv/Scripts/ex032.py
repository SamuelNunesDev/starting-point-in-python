n = int(input('Digite o ano para saber se ele foi, é ou será bissesto: '))
if n % 400 == 0:
    print(f'O ano de {n} é bissesto!')
else:
    if n % 4 == 0 and n % 100 != 0:
        print(f'O ano de {n} é bissesto!')
    else:
        print(f'O ano de {n} não é bissesto!')
