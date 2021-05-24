l = list()
for c in range(1, 4):
    n = int(input(f'Digite o {c}º número: '))
    l.append(n)
print(f'O maior número entre eles é o {max(l)} e o menor é {min(l)}')
