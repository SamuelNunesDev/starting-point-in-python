def metade(v):
    return v / 2


def dobro(v):
    return v * 2


def aumentar(v, p):
    return v * p / 100 + v


def diminuir(v, p):
    return v - v * p / 100


def moeda(v, c=True):
    if c == True:
        p = str(f'{v:.2f}')
        return f'R${p.replace(".", ",")}'
    else:
        return v


def resumo(v, a, r):
    print(f'{"-" * 50} \n{"Resumo do Valor":^50}\n{"-" *50}')
    print(f'{"Preço análisado":.<41} {moeda(v)}')
    print(f'{"Dobro do preço":.<41} {moeda(dobro(v))}')
    print(f'{"Metade do preço":.<41} {moeda(metade(v))}')
    print(f'{a}{"% de aumento":.<39} {moeda(aumentar(v, a))}')
    print(f'{r}{"% de redução":.<39} {moeda(diminuir(v, r))}')
    print('-' * 50)

