from time import sleep

for c in range(10, -1, -1):
    print(f'Faltam {c} segundos para o estouro dos fogos!')
    sleep(1)
print('BOOM!')
