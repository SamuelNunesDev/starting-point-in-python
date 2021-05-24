from urllib import request

try:
    request.urlopen('http://www.pudim.com.br')
except:
    print('\033[1:31mHouve um erro ao tentar acessar o site!')
else:
    print('\033[1:33mConsegui acessar o site com sucesso!')
