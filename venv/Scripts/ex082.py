l = list()
lp = list()
li = list()
while True:
    n = int(input('Digite um número: '))
    l.append(n)
    if n % 2 == 0:
        lp.append(n)
    else:
        li.append(n)
    while True:
        c = input('Quer continuar? [S/N]').strip().lower()
        if c in 'sn':
            break
    if c in 'n':
        print(f'Lista que contém todos os números digitados: {l} \nLista que contém apenas os números pares digitados '
              f'{lp} \nLista que contém apenas os números ímpares digiados {li}')
        break
