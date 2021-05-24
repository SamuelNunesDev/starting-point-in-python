l = list()
for c in range(1, 5):
    a = input(f'Qual o nome do {c}º aluno? ')
    l.append(a)
print(f'A ordem de apresentação será {sorted(l)}')
