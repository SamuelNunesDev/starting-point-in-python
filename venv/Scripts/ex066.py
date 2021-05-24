l = list()
while True:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n != 999:
        l.append(n)
    else:
        print(f'Você digitou {len(l)} números e a soma entre eles é {sum(l)}')
        break
