def fatorial(n, show=False):
    '''
        -> Calcula o fatorial de um número.
    :param n: Valor a ser calculado o fatorial.
    :param show: Opção de ocultar ou mostrar o processo do cálculo.
    :return: O fatorial do número n.
    '''
    f = 1
    if show == True:
        for c in range(n, 1, -1):
            f *= c
            print(f'{c} x ', end='')
        print(f'1 = ', end='')
        return f
    else:
        for c in range(n, 1, -1):
            f *= c
        return f


print(fatorial(5))
help(fatorial)