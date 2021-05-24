n = input('Digite seu nome completo: ').strip()
e = n.count(' ')
pn = n.split()
print(f'Seu nome completo em letras maiúsculas é {n.upper()} \nem letras minúsculas é {n.lower()}. \nSeu nome '
      f'completo possui {len(n)-e} letras \ne seu primeiro nome possui {len(pn[0])} letras!')
