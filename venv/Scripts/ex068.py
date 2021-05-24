from random import choice

l = list(range(0, 11))
w = 0
while True:
    pc = choice(l)
    c = input('Par ou Ímpar? [P/I] ').strip().lower()
    p1 = int(input('Digite o valor que deseja jogar: '))
    if c in 'p' and (pc + p1) % 2 == 0:
        w += 1
        print(f'PARABÉNS! Você venceu! O pc jogou {pc} \nTotal de vitórias: {w}')
    elif c in 'i' and (pc + p1) % 2 != 0:
        w += 1
        print(f'PARABÉNS! Você venceu! O pc jogou {pc} \nTotal de vitórias: {w}')
    else:
        print(f'Você perdeu! O pc jogou {pc} \nTotal de vitórias {w}')
        break
