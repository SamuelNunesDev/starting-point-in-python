l = list()
for c in range(1, 6):
    l.append(int(input(f'Digite o {c}º valor: ')))
print(f'O maior valor digitado foi {max(l)} e sua posição na lista é {l.index(max(l))} \nO menor valor digitado foi '
      f'{min(l)} e sua posição na lista é {l.index(min(l))}')
