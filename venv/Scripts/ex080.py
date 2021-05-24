l = list()
for c in range(1, 6):
    n = float(input(f'Digite o {c}º valor: '))
    if len(l) == 0 or n > l[-1]:
        l.append(n)
    else:
        pos = 0
        while pos <= len(l):
            if n < l[pos]:
                l.insert(pos, n)
                break
            else:
                pos += 1
print(f'A lista ordenada fica {l}')
