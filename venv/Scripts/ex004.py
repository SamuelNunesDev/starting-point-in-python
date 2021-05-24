x = (input('Digite algo: '))
print(f'O tipo primitivo do texto digitado é {x.__class__}')

if x.isalnum():
    print('O texto digitado é alfanumérico, ', end='')
else:
    print('O texto digitado não é alfanumérico, ', end='')
if x.isalpha():
    print('é alfabético, ', end='')
else:
    print('não é alfabético, ', end='')
if x.isnumeric():
    print('é numérico, ', end='')
else:
    print('não é numérico, ', end='')
if x.isdecimal():
    print('é decimal, ', end='')
else:
    print('não é decimal, ', end='')
if x.islower():
    print('está somente em letras minúsculas, ')
else:
    print('não está somente em letras minúsculas, ')
if x.isupper():
    print('está somente em letras maiúsculas, ', end='')
else:
    print('não está somente em letras maiúsculas, ', end='')
if x.istitle():
    print('está capitalizado, ', end='')
else:
    print('não está capitalizado, ', end='')
if x.isspace():
    print('e é um espaço vazio!')
else:
    print('e não é um espaço vazio!')
