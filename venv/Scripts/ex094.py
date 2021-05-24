l = list()
s = 0
while True:
    nome = input('Qual o nome da pessoa? ')
    idade = int(input(f'Qual a idade de {nome}? '))
    s += idade
    while True:
        sexo = input(f'Qual o sexo de {nome}? [M/F] ').strip().lower()
        if sexo in 'mf':
            break
    l.append({'Nome' : nome, 'Idade' : idade, 'sexo' : sexo})
    while True:
        c = input('Deseja continuar? [S/N] ').strip().lower()
        if c in 'sn':
            break
    if c in 'n':
        print(f'Foram cadastradas {len(l)} pessoas.')
        lm = list()
        media = s / len(l)
        lmedia = list()
        for pos, k in enumerate(l):
            for q, v in k.items():
                if q in "Idade" and v > media:
                    lmedia.append(l[pos]["Nome"])
                if q in "sexo" and v in 'f':
                    lm.append(l[pos]["Nome"])
        print(f'A média de idade do grupo é de {media} anos. \nListagem de todas as mulheres: {lm} \nListagem com todas'
              f'as pessoas com idade acima da média do grupo: {lmedia}')
        break
