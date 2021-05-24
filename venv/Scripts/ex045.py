from random import choice

l = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(l)
while True:
    print('[1] PARA JOGAR PEDRA \n[2] PARA JOGAR PAPEL \n[3] PARA JOGAR TESOURA')
    p1 = input('Digite sua escolha: ')
    if p1 in '1' and pc in 'PEDRA':
        print('O PC também jogou pedra! EMPATOU!')
        break
    elif p1 in '1' and pc in 'PAPEL':
        print('O PC jogou papel! Você perdeu!')
        break
    elif p1 in '1' and pc in 'TESOURA':
        print('O PC jogou tesoura! Você venceu!')
        break
    elif p1 in '2' and pc in 'PEDRA':
        print('O PC jogou pedra! Você venceu!')
        break
    elif p1 in '2' and pc in 'PAPEL':
        print('O PC também jogou papel! EMPATOU!')
        break
    elif p1 in '2' and pc in 'TESOURA':
        print('O PC jogou tesoura! Você perdeu!')
        break
    elif p1 in '3' and pc in 'PEDRA':
        print('O PC jogou pedra! Você perdeu!')
        break
    elif p1 in '3' and pc in 'PAPEL':
        print('O PC jogou papel! Você venceu!')
        break
    elif p1 in '3' and pc in 'TESOURA':
        print('O PC também jogou tesoura! EMPATOU!')
        break
    else:
        print('DIGITE UMA OPÇÃO VÁLIDA!')
