def triangulo():
    l = list()
    for c in range(1, 4):
        r = float(input(f'Digite o comprimento da {c}ª reta: '))
        l.append(r)
    if l[0] < l[1] + l[2] and l[1] < l[0] + l[2] and l[2] < l[0] + l[1]:
        print('É possível a formação do triângulo!')
        return l
    else:
        print('Não é possível a formação do triângulo!')
        return ''