t = (int(input('Digite um número inteiro: ')), int(input('Digite um número inteiro: ')),
     int(input('Digite um número inteiro: ')), int(input('Digite um número inteiro: ')))
print(f'O valor 9 apareceu {t.count(9)} vezes \nO primeiro valor 3 foi digitado na posição {t.index(3)} \nOs números '
      f'pares digitados foram: ', end='')
for c in range(0, len(t)):
    if t[c] % 2 == 0:
        print(t[c], end=' ')
