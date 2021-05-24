from random import randint
from time import  sleep
from operator import itemgetter

d = {'Jogador 1' : randint(1, 6), 'Jogador 2' : randint(1, 6), 'Jogador 3' : randint(1, 6), 'Jogador 4' : randint(1, 6)}
input('Aperte qualquer tecla para jogar os dados.')
for k, v in d.items():
    print(f'O {k} tirou o número {v} no dado!')
    sleep(1)
d = sorted(d.items(), key=itemgetter(1), reverse=True)
print(f'O dicionário em ordem fica: {d}')
print('RANKING: \n')
for k, v in enumerate(d):
    print(f'{k + 1}º lugar: {v[0]} com o número {v[1]}')
