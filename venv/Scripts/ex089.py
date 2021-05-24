l = [[], [], []]
while True:
    l[0].append(input('Qual o nome do aluno? ').strip().capitalize())
    n1 = float(input(f'Qual a primeira nota do aluno? '))
    n2 = float(input(f'Qual o segunda nota do aluno? '))
    l[1].append((n1 + n2) / 2)
    l[2].append(n1)
    l[2].append(n2)
    while True:
        c = input('Deseja continuar? [S/N] ').strip().lower()
        if c in 'sn':
            break
    print('-' * 30)
    if c in 'n':
        print(f'{"Nome":^9}{"Média":>21}')
        for i in enumerate(l[0]):
            print(f'{i[1]:.<24} {l[1][i[0]]:>5.2f}')
        print('-' * 30)
        break
while True:
    while True:
        c2 = input('Deseja ver as notas de algum aluno? [S/N] ').strip().lower()
        if c2 in 'sn':
            break
    if c2 in 'n':
        print('FINALIZANDO...')
        break
    notas = input('Qual o nome do aluno? ').strip().capitalize()
    if notas in l[0]:
        if l[0].index(notas) == 0:
            print(f'Aluno: {notas.capitalize()} \nNota 1: {l[2][0]} \nNota 2: {l[2][1]}')
        else:
            num_list = l[0].index(notas) * 2
            print(f'Aluno: {notas.capitalize()} \nNota 1: {l[2][num_list - 1]} \nNota 2: {l[2][num_list]}')
