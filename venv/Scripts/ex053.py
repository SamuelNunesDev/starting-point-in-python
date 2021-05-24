fi = input('Digite uma frase pra saber se ela é um palíndromo: ')
f = fi.replace(' ', '')
fp = ''
for l in f[::-1]:
    fp += l
if fp in f:
    print(f'A frase "{fi}" é um palíndromo!')
else:
    print(f'A frase "{fi}" não é um palíndromo!')
