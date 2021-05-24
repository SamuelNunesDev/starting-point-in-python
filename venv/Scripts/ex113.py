def leiaint():
    while True:
        n = input('Digite um número inteiro: ')
        if n.isnumeric():
            return n
        else:
            print('\033[1:31mERRO! Digite um número inteiro válido!\033[m')


def leiafloat():
    while True:
        n = input('Digite um número real: ')
        if n.isnumeric():
            return float(n)
        elif n.count('.') == 1 and n.replace('.','').isnumeric():
            return n
        else:
            print('\033[1:31mERRO! Digite um número real válido!\033[m')


print(f'O valor inteiro digitado foi {leiaint()} e o real {leiafloat()}')
