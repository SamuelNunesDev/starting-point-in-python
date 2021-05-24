p = float(input('Digite sem peso em Kg: '))
a = float(input('Digite sua altura em metros: '))
imc = p / a ** 2
if imc < 18.5:
    print(f'Seu IMC atual é {imc:.1f}, você está abaixo do peso!')
elif imc < 25:
    print(f'Seu IMC atual é {imc:.1f}, você está no peso ideal!')
elif imc < 30:
    print(f'Seu IMC atual é {imc:.1f}, você está no sobrepeso!')
elif imc < 40:
    print(f'Seu IMC atual é de {imc:.1f}, você está com obesidade!')
else:
    print(f'Seu IMC atual é de {imc:.1f}, você está com obesidade mórbida!')
