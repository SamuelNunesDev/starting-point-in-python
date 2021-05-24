from datetime import date

p = 0
for c in range(1, 8):
    i = int(input(f'Em qual ano a {c}ª pessoa nasceu? '))
    if date.today().year - i >= 18:
        p += 1
print(f'{p} pessoas atingiram a maioridade!')
