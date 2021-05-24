from datetime import date


def voto(n):
    if date.today().year - n < 18:
        return f'Você possui {date.today().year - n} anos, por esse motivo o voto foi NEGADO!'
    elif date.today().year - n > 65:
        return f'Você possui {date.today().year - n} anos, por esse motivo o voto é OPCIONAL!'
    else:
        return f'Você possui {date.today().year - n} anos, por esse motivo o voto é OBRIGATÓRIO!'


print(voto(int(input('Digite a data do seu nascimento: '))))
