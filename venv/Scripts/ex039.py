from datetime import date

hoje = date.today().year
ano = input('Digite a data do seu nascimento: ').strip()
ano = ano[6:]
ano = hoje - int(ano)
if ano == 18:
    print('Está na hora de se alistar!')
elif ano > 18:
    print(f'Já passou {ano - 18} ano(s) que você deveria ter se alistado!')
else:
    print(f'Falta {18 - ano} ano(s) para você se alistar!')
