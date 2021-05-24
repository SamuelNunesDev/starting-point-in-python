def maior(*n):
    try:
        l = len(n)
        m = max(n)
    except:
        l = 0
    print(f'{"-=" * 25} \nAnálisando os valores passados...')
    for i in n:
        print(f'{i} ', end='')
    print(f'Foram informados {l} valores ao todo! \nO maior valor informado foi {l}')

maior(1, 2, 3)
maior()
