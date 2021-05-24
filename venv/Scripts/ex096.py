def area(l, c):
    return f'A área do terreno {l}x{c} é de {l * c:.2f} m²'

print(area(float(input('Qual a largura do terreno? ')), float(input('Qual o comprimento do terreno? '))))
