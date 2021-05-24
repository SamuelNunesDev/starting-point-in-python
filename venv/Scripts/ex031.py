p = int(input('Qual a distância da viagem? '))
if p >= 200:
    print(f'O valor da passagem da viagem de {p}km é de R${p * 0.45:.2f}')
else:
    print(f'O valor da passagem da viagem de {p}km é de R${p * 0.5:.2f}')
