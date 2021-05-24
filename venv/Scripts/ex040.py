n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print(f'Média {m} \no aluno foi REPROVADO!')
elif 7 > m >= 5 :
    print(f'Média {m} \no aluno está de RECUPERAÇÃO!')
else:
    print(f'Média {m} \no aluno foi APROVADO!')
