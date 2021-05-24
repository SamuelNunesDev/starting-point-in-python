n1 = int(input('Quantos termos da sequencia de fibonacci deseja ver? '))
t1 = 0
t2 = 1
print(f'{t1} - {t2} ', end='')
for c in range(0, n1):
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'- {t3}', end=' ')
print('- FIM')
