from random import choice

l = list(range(0, 11))
pc = choice(l)
p = 0
while True:
    p1 = int(input('Tente advinhar o número que estou pensando: '))
    p += 1
    if p1 == pc:
        print(f'PARABÉNS! Eu estava pensando no número {pc} mesmo! \nVocê precisou de {p} palpites para acertar!')
        break
    elif pc > p1:
        print(f'Um pouco MAIS!')
    else:
        print(f'Um pouco MENOS!')
