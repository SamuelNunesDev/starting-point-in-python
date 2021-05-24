s = float(input('Digite o seu salário atual: '))
if s > 1250:
    print(f'O seu salário com um aumento de 10% será R${(s * 10 / 100) + s:.2f}')
else:
    print(f'O seu salário com um aumento de 15% será R${(s * 15 / 100) + s:.2f}')
