from math import floor

n = int(input('Digite um número: '))
ni = n
um = floor(n / 1000)
n = n - um * 1000
c = floor(n / 100)
n = n - c * 100
d = floor(n / 10)
n = n - d * 10
print(f'O número {ni} possui: \n{um} unidade(s) de milhar \n{c} centenas \n{d} dezenas \n{n} unidades.')
