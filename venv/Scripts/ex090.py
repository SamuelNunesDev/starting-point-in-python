d = dict()
d["nome"] = input('Nome: ')
d["media"] = float(input('Média: '))
print(f'O nome é {d["nome"]} \nA média é {d["media"]}')
if d["media"] < 4:
    print('A situação atual é REPROVADO!')
elif d["media"] < 7:
    print('A situação atuai é RECUPERAÇÃO!')
else:
    print('A situação atual é APROVADO!')
