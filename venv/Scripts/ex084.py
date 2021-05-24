l = list()
lp = list()
while True:
    l.append(input('Digite o nome: '))
    lp.append(float(input('Digite o peso: ')))
    while True:
        c = input('Deseja continuar? [S/N] ').strip().lower()
        if c in 'sn':
            break
    if c in 'n':
        print(f'Foram cadastradas {len(l)} pessoas. \nO menor peso foi de {min(lp)} e o maior {max(lp)}')
        break
