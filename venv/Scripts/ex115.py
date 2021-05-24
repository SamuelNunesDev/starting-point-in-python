from Utilitários.dado import ver_pessoas, cadastrar
from os import listdir

while True:
    print(f'{"-" * 50}\n{"MENU PRINCIPAL":^50}\n{"-" * 50}')
    print('\033[1:33m1\033[m - \033[1:34mVer pessoas cadastradas')
    print('\033[1:33m2\033[m - \033[1:34mCadastrar nova pessoa')
    print(f'\033[1:33m3\033[m - \033[1:34mSair do programa\033[m\n{"-" * 50}')
    while True:
        o = input('Sua opção: ')
        if o in '123' and o not in '':
            break
        else:
            print('\033[1:31mDigite uma opção válida!\033[m')
    if 'pessoas.txt' not in listdir('.\\'):
        a = open('pessoas.txt', 'wt+')
        a.close()
    if o in '1':
        txt = ver_pessoas()
        if txt[1] is True:
            print('-' * 50)
            print(f'\n {"Nome":<42}{"Idade"}')
            for pessoa in txt[0]:
                pessoa = str(pessoa)
                print(f'{pessoa[:pessoa.index(";")]:.<41} {pessoa[pessoa.index(";") + 1:pessoa.index(";") + 3]} anos')
            print()
    elif o in '2':
        cadastrar(input('Nome: '), input('Idade: '))
    elif o in '3':
        print(f'{"-" * 50}\n{"Até logo!":^50}\n{"-" * 50}')
        break
