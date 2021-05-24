n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
while True:
    print('\nO que deseja fazer? \n')
    print('[1] Somar \n[2] Subtrair \n[3] Maior número digitado \n[4] Novos números \n[5] Sair do programa')
    o = input('Digite a operação: ')
    if o in '1':
        print(f'O valor da soma entre os números {n1} e {n2} é {n1 + n2}')
    elif o in '2':
        print(f'O valor da subtração entre os números {n1} e {n2} é {n1 - n2}')
    elif o in '3':
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}')
        elif n1 < n2:
            print(f'O maior número entre {n1} e {n2} é {n2}')
        else:
            print(f'Não existe maior valor entre {n1} e {n2}, pois são iguais!')
    elif o in '4':
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif o in '5':
        print('FINALIZANDO...')
        break
    else:
        print('Erro, digite uma opção válida!')
