from moeda import *

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p:.2f} equivale a R${metade(p):.2f}')
print(f'O dobro de R${p:.2f} equivale a R${dobro(p):.2f}')
print(f'Aumentando R${p:.2f} em 10% temos R${aumentar(p, 10):.2f}')
print(f'Diminuindo R${p:.2f} em 13% temos R${diminuir(p, 13):.2f}')
