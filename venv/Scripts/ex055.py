l = list()
for c in range(1, 6):
    l.append(float(input(f'Qual o peso da {c}º pessoa? ')))
print(f'O maior peso foi {max(l):.1f}Kg e o menor foi {min(l):.1f}Kg')
