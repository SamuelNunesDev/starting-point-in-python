from random import randint

l = list()
n = int(input('Quantos jogos você quer gerar? '))
for c in range(1, n + 1):
    l.append([randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)])
for i in enumerate(l):
    print(f'Palipite {i[0] + 1}: {i[1]}')
print('Boa sorte!')
