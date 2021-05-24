l = list()
c = 's'
while True:
    n = int(input('Digite um número: '))
    if c in 's':
        l.append(n)
    c = input('Deseja continuar? [S/N] ').strip().lower()
    if c in 'n':
        print(f'A média entre os números digitados foi {sum(l) / len(l):.2f} \nO maior número digitado foi {max(l)} '
              f'e o menor foi {min(l)}')
        break
