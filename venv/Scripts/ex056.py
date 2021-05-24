med = 0
h = ''
m = 0
hi = 0
for c in range(1, 5):
    n = input(f'Qual o nome da {c}ª pessoa? ')
    s = input(f'Qual o sexo da {c}ª pessoa [M/F]? ').strip().lower()
    i = int(input(f'Qual a idade da {c}ª pessoa? '))
    if s in 'f' and i < 20:
        m += 1
    if s in 'm' and i > hi:
        hi = i
        h = n
    med += i
print(f'A média de idade do grupo é de {med / 4:.1f} anos!')
print(f'O homem mais velho do grupo é o {h}')
print(f'Tem {m} mulher(es) com a idade menor de 20 anos.')
