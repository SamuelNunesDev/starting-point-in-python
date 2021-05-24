def notas(*n, sit=False):
    '''
    -> Função para mostrar as notas de uma turma e definir a situação.
    :param n: valores das notas da turma.
    :param sit: define se deve ou não mostrar a situação da turma.
    :return: dicionário contendo a quantidade, a média, a maior e a menor nota da turma.
    '''
    d = dict()
    d['quantidade'] = len(n)
    d['maior'] = max(n)
    d['menor'] = min(n)
    d['média'] = sum(n) / len(n)
    if sit == True:
        if d['média'] >= 7:
            d['situação'] = 'Boa'
        elif d['média'] < 4:
            d['situação'] = 'Ruim'
        else:
            d['situação'] = 'Razoável'
    return d


print(notas(1, 2, 3, sit=True))
help(notas)