from ex035 import triangulo

l = triangulo()
if len(l) != 0:
    if l[0] == l[1] == l[2]:
        print('O triângulo será EQUILÁTERO!')
    elif l[0] == l[1] or l[0] == l[2] or l[1] == l[2]:
        print('O triângulo será ISÓSCELES!')
    else:
        print('O triângulo será ESCALENO!')
