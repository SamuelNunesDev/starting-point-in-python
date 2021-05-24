n = int(input('Digite um número inteiro para saber o seu fatorial: '))
f = 1
for c in range(n, 0, -1):
    f *= c
    if c == n:
        print(f'{n}! = {c}', end='')
    elif c == 1:
        print(f'x1 = {f}')
    else:
        print(f'x{c}', end='')
