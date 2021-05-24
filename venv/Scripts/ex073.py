t = ('Flamengo', 'Internacional', 'Atlético - MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos',
     'Athletico - PR', 'Bragantino', 'Ceará - SC', 'Corinthians', 'Atlético - GO', 'Bahia', 'Sport Recife',
     'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Os 5 primeiros colocados são {t[0:5]} \nOs 4 últimos colocados são {t[-4:]} \nLista dos times em ordem '
      f'alfabética: {sorted(t)} \nO Bragantino está na {t.index("Bragantino") + 1}ª posição')
