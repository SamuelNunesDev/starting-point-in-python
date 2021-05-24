l = list()
while True:
    n = input('Digite um valor: ')
    if n in l:
        print('Valor já cadastrado!')
    else:
        print('Valor cadastrado com sucesso!')
        l.append(n)
    while True:
        c = input('Deseja continuar? [S/N] ').strip().lower()
        if c in 'sn':
            break
    if c in 'n':
        print(sorted(l))
        break
