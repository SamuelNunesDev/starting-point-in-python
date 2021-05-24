t = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
     'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 50, f'\n{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)
c = True
for i in t:
    if c == True:
        print(f'{i:.<41}', end='R$')
        c = False
    else:
        print(f' {i:>6.2f}')
        c = True
