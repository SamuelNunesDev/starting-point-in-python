while True:
    n = int(input('Deseja ver a tabuada de qual número? '))
    if n >= 0:
        for c in range(0, 11):
            print(f'{n} x {c} = {n * c}')
    else:
        print('FINALIZANDO...')
        break
