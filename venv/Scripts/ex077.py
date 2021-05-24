t = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
     'programador', 'futuro')
for palavra in t:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
