n = int(input('Digite um número para saber se ele é primo ou não: '))
f = False
while n in range(n - 1, 1, -1):
    if n % c == 0:
        f = False
        break
    else:
        f = True
        break
if f == False:
    print(f'{n} não é um número primo!')
else:
    print(f'{n} é um número primo!')
