l = [[], [], []]
f = 0
lp = list()
tc = 0
for c in range(0, 3):
    for pos in range(0, 3):
        n = int(input(f'Digite um valor para a posição ({c}, {pos}): '))
        l[c].append(n)
        if n % 2 == 0:
            lp.append(n)
        if pos == 2:
            tc += n
for i in l:
    print()
    for x in i:
        print(f'{x}', end=' ')
print(f'\nOs números pares da matriz são: {lp} \nA soma dos valores da terceira coluna é {tc} \nE o maior valor da '
      f'segunda linha é {max(l[1])}')
