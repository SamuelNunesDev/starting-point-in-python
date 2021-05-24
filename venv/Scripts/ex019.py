from random import choice
from time import sleep

l = list()
for c in range(1, 5):
    a = input(f'Digite o nome do {c}º aluno: ')
    l.append(a)
print('\033[1:33mSorteando...\033[m')
sleep(2)
print(f'O aluno escolhido foi \033[1:32m{choice(l)}!')
