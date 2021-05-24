e = input('Digite a expressão: ')
c = 0
cond = 0
while c < len(e):
    if e[c] in '(':
        cond += 1
    elif e[c] in ')':
        cond -= 1
    if cond < 0:
        break
    c += 1
if cond != 0:
    print('A expressão está incorreta!')
else:
    print('A expressão está correta!')
