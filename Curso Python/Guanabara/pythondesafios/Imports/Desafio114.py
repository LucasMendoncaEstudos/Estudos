'''Crie um código em Python que verifique se o site Pudim está acessível pelo computador utilizado.'''

import urllib
import urllib.request

try:
    site : urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso')