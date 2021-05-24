pt = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão da P.A.: '))
pa = pt
p = True
cond = False
while True:
    f = int(input('Quantos termos da P.A. deseja ver? '))
    if f > 0:
        if p == True:
            print(f'({pt}', end='')
            p = False
        else:
            print(f'({pa}', end='')
        for c in range(0, f):
            pa += r
            print(f', {pa}', end='')
            if c == f - 1:
                print(')')
    else:
        print('FINALIZANDO...')
        break
