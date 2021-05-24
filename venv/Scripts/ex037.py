print('Conversor de números\n')
while True:
	n = input('Digite um número inteiro: ')
	if n.isnumeric():
		print('Escolha uma opção para conversão: \n[1] para binário \n[2] para octal \n[3] para hexadeximal')
		break
	else:
		print('Digite uma opção válida!')
while True:
	o = input('Digite uma opção para conversão: ')
	if o.isnumeric():
		o = int(o)
		n = int(n)
		if o == 1:
			nb = str(bin(n))
			nb = nb[2:]
			print(f'O número {n} em binário é: {nb}')
			break
		elif o == 2:
			no = str(oct(n))
			no = no[2:]
			print(f'O número {n} em octal é: {no}')
			break
		elif o == 3:
			nh = str(hex(n))
			nh = nh[2:]
			print(f'O número {n} em hexadecimal é: {nh}')
			break
		else:
			print('Escolha uma opção válida: \n[1] para binário \n[2] para octal \n[3] para hexadeximal')
	else:
		print('Escolha uma opção válida: \n[1] para binário \n[2] para octal \n[3] para hexadeximal')
