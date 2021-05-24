h = 0
i = 0
m = 0
while True:
    n = int(input('Qual a idade da pessoa? '))
    if n >= 18:
        i += 1
    s = input('Qual o sexo da pessoa? [M/F] ').strip().lower()
    if s in 'm':
        h += 1
    if s in 'f' and n < 20:
        m += 1
    c = input('Deseja continuar? [S/N] ').strip().lower()
    if c in 'n':
        print(f'{i} pessoas tem mais de 18 anos. \nForam cadastrados {h} homens \n{m} mulheres tem menos de 20 anos.')
        break
