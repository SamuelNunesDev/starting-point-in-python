from moeda import *

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p, False)} equivale a {moeda(metade(p), False)}')
print(f'O dobro de {moeda(p, True)} equivale a {moeda(dobro(p), True)}')
print(f'Aumentando {moeda(p, True)} em 10% temos {moeda(aumentar(p, 10), True)}')
print(f'Diminuindo {moeda(p, False)} em 13% temos {moeda(diminuir(p, 13), False)}')
