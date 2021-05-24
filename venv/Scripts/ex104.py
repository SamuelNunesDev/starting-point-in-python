def leiaint():
    while True:
        n = input('Digite um número inteiro: ')
        if n.isnumeric():
            return f'Você digitou o número {n}'
            break
        else:
            print('\033[1:31mERRO! Digite um número inteiro válido!\033[m')


print(leiaint())
