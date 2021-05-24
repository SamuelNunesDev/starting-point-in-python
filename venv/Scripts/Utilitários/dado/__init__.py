def leiadinheiro(txt):
    while True:
        v = input(txt).strip()
        try:
            if v[-4] in '':
                print('\033[1:31mERRO! Digite um preço válido!\033[m')
            else:
                if v[-3:-2] in ',' and v.count(',') == 1:
                    return float(v.replace(',', '.'))
                else:
                    print('\033[1:31mERRO! Digite um preço válido!\033[m')
        except:
            print('\033[1:31mERRO! Digite um preço válido!\033[m')


def ver_pessoas():
    a = open('pessoas.txt')
    s = a.readlines()
    a.close()
    if len(s) == 0:
        print('Não há nenhuma pessoa cadastrada!')
        return s, False
    else:
        return s, True


def cadastrar(n, i):
    a = open('pessoas.txt', 'at')
    s = f'{n};{i}\n'
    a.write(s)
    a.close()
    print(f'{n} cadastrado com sucesso!')
