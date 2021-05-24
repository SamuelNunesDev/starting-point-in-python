def escreva(t):
    t = f"{'~' * (len(t) + 2)} \n {t}\n{'~' * (len(t) + 2)}"
    return t


print(escreva(input('Digite uma frase: ')))
