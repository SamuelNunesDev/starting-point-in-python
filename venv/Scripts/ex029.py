v = int(input('Qual a velocidade atual do veículo? '))
if v > 80:
    print(f'VELOCIDADE MÁXIMA EXCEDIDA! Multa de R${(v - 80) * 7:.2f} aplicada!')
else:
    print(f'Velocidade atual: {v}kmh. Dirija com cuidado! Boa viagem!')
