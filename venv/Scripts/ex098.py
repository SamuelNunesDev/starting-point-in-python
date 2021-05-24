from time import sleep


def contador(i, f, p):
    if p == 0:
        if i > f:
            p = -1
        else:
            p = 1
    print(f'{"-=" * 25} \nContagem de {i} a {f} de {p} em {p}:')
    for c in range(i, f, p):
        print(f'{c} ', end='')
        sleep(1)
    print()
    return 'Fim'


print(f'{"-=" * 25} \nContagem de 0 a 10 de 1 em 1:')
for c in range(0, 11):
    print(f'{c} ', end='')
    sleep(1)
print(f"\n{'-=' * 25} \nContagem de 10 a 0 de 2 em 2:")
for c in range(10, -1, -2):
    print(f'{c} ', end='')
    sleep(1)
print(f'\n{"-=" * 25} \nAgora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
print(contador(i, f, p))
