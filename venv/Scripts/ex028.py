from random import randint

n = randint(1, 4)
r = int(input('Digite o número que eu estou pensando: '))
if n == r:
    print(f'PARABÉNS! Eu também pensei no número {n}!')
else:
    print(f'VOCÊ ERROU! Eu pensei no número {n}!')
