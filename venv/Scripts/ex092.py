from datetime import date

d = dict()
d["Nome"] = input('Nome: ')
d["Idade"] = int(input('Ano de nascimento: '))
d["Idade"] = date.today().year - d["Idade"]
d["CTPS"] = int(input('CTPS: (0 não tem)'))
if d["CTPS"] != 0:
    d["Ano de contratação"] = int(input('Ano de contratação: '))
    d["Salario"] = float(input('Salário: R$'))
    d["Aposentadoria"] = d["Idade"] + 35
    for k, v in d.items():
        if k in 'Salario':
            print(f'{k}: R${v:.2f}')
        elif k in 'Aposentadoria':
            print(f'{k}: {v} anos')
        else:
            print(f'{k}: {v}')
else:
    for k, v in d.items():
        print(f'{k}: {v}')
