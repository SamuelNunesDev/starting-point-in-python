d = {}
d["Nome"] = input('Qual o nome do jogador? ')
d["Gols"] = list()
n = int(input(f'Quantas partidas {d["Nome"]} jogou? '))
for c in range(1, n + 1):
    d['Gols'].append(int(input(f'Quantos gols {d["Nome"]} fez na {c}ª partida? ')))
d["Total"] = sum(d['Gols'])
print('-=' * 30, f'\n{d}')
print('-=' * 30)
for k, v in d.items():
    print(f'O campo {k} tem valor {v}')
print(f'O jogador {d["Nome"]} jogou {n} partidas!')
for i in enumerate(d["Gols"]):
    print(f'   -> Na {i[0] + 1}ª partida fez {d["Gols"][i[0]]} gols')
print(f'Foi um total de {sum(d["Gols"])}')
