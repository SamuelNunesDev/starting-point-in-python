def ficha(n='<desconhecido>', g=0):
    if n in '':
        n = '<desconhecido>'
    if g in '':
        g = '0'
    return f'O jogador {n} fez {g} gols no campeonato.'


print(ficha(input('Nome do jogador: '), input('Número de gols: ')))
