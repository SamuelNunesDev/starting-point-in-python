while True:
    c = input('Digite o sexo [M/F] : ').strip().lower()
    if c in 'mf':
        break
    else:
        print('Erro! Digite uma letra válida! ')
print(f'Você selecionou o sexo "{c.upper()}"')
