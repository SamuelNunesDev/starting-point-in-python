n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print(f'O número {n1} é maior que {n2}')
elif n2 > n1:
    print(f'O número {n2} é maior que {n1}')
else:
    print('Não existe valor maior, os números são iguais!')
