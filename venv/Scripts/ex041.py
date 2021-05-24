from datetime import date

hoje = date.today().year
ano = input('Digita a data do seu nascimento: ')
ano = hoje - int(ano[6:])
if ano < 9:
    print(f'O atleta tem {ano} anos, logo pertence a categoria MIRIM!')
elif ano < 14:
    print(f'O atleta tem {ano} anos, logo pertence a categoria INFANTIL!')
elif ano < 19:
    print(f'O atleta tem {ano} anos, logo pertence a categoria JÚNIOR!')
elif ano < 20:
    print(f'O atleta tem {ano} anos, logo pertence a categoria SÊNIOR!')
else:
    print(f'O atleta tem {ano} anos, logo pertence a categoria MASTER!')
