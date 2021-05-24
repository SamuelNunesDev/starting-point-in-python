l = [list(), list()]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 ==0:
        l[0].append(n)
    else:
        l[1].append(n)
print(f'A lista com os números pares é {sorted(l[0])} \nA lista com os valores ímpares é {sorted(l[1])}')
