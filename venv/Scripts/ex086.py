l = [[], [], []]
f = 0
for c in range(0, 3):
    for pos in range(0, 3):
        l[c].append(input(f'Digite um valor para a posição ({c}, {pos}): '))
for i in l:
    print()
    for x in i:
        print(f'{x}', end=' ')
