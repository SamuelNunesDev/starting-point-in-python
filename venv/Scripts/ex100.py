from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores... ', end='')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(numeros[c], end=' ')
        sleep(1)
    print('PRONTO!')


def somapar():
    print(f'Somando os valores pares de {numeros},', end='')
    s = 0
    for i in numeros:
        if i % 2 == 0:
            s += i
    print(f' temos {s}')


numeros = list()
sorteia()
somapar()
