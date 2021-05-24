pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da P.A.:' ))
for c in range(2, 12):
    if c == 2:
        s = pt + r
        print(f'({pt}, {s}, ', end='')
    elif c < 11:
        s += r
        print(f'{s}, ', end='')
    else:
        s += r
        print(f'{s})')
