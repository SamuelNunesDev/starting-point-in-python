n = int(input('Qual o valor que deseja sacar? '))
cinquenta = n // 50
n = n - cinquenta * 50
vinte = n // 20
n = n - vinte * 20
dez = n // 10
n = n - dez * 10
print(f'Você receberá: \n{cinquenta} cédulas de R$50,00 \n{vinte} cédulas de R$20,00 \n{dez} cédulas de R$10,00 \n{n} '
      f'cédulas de R$1,00')
