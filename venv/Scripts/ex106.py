print('\033[1:44m-=' * 25, f'\n{"Sistema de ajuda PyHelp":^50}')
print('-=' * 25)
while True:
    n = input('\033[mFunção ou Biblioteca -> \033[1:31m').strip()
    if n in 'FIMfimFim':
        print('\033[7:30:41m-=' * 25, f'\n{"Até Logo!":^50}')
        print('-=' * 25)
        break
    help(n)
