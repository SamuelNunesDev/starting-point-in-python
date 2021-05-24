l = list()
d = {}
while True:
    d["Nome"] = input('Qual o nome do jogador? ')
    d["Gols"] = list()
    n = int(input(f'Quantas partidas {d["Nome"]} jogou? '))
    for c in range(1, n + 1):
        d['Gols'].append(int(input(f'Quantos gols {d["Nome"]} fez na {c}ª partida? ')))
    d["Total"] = sum(d['Gols'])
    l.append(d.copy())
    while True:
        cond = input('Deseja continuar? [S/N] ').strip().lower()
        if cond in 'sn' and cond not in ' ':
            break
    print('-=' * 40)
    if cond in 'n':
        break
print(f'{"ID":^4} {"Nome":^10} {"Gols":>8} {"Total":>13}')
for pos, item in enumerate(l):
    print(f' {pos + 1}   ', end='')
    for key, itens in item.items():
        if key in 'Nome':
            print(f'{itens:^10}    ', end='')
        elif key in 'Gols':
            print(f'{str(itens):<15}', end='')
        elif key in 'Total':
            print(f'{itens}')
print('-=' * 40)
while True:
    cond = input('Mostrar dados de qual jogador? (0 para sair) ')
    if cond.isnumeric():
        cond = int(cond)
        if 0 < cond <= len(l):
            print(f'     Detalhamento do jogador {l[cond - 1]["Nome"]}')
            for pos, i in enumerate(l[cond - 1]["Gols"]):
                print(f'  -> Na {pos + 1}ª partida {l[cond - 1]["Nome"]} fez {i} gols.')
            print(f'Um total de {sum(l[cond - 1]["Gols"])} gols!')
            print('-=' * 40)
        elif cond == 0:
            print('FINALIZANDO...')
            break
        else:
            print('Digite um ID válido!')
    else:
        print('Digite um ID válido!')
