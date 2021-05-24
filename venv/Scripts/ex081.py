l = list()
while True:
    l.append(float(input('Digite um número: ')))
    while True:
        c = input('Quer continuar? [S/N] ').strip().lower()
        if c in 'sn':
            break
    if c in 'n':
        print(f'Foram digitados {len(l)} números. \nA lista em ordem decrescente é {sorted(l, reverse=True)}')
        if 5 in l:
            print('O número 5 está na lista.')
        else:
            print('O número 5 não está na lista.')
        break
