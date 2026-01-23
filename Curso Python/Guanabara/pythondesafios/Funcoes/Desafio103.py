"""Crie um programa que contenha uma função chamada Ficha(), que recebe dois parâmetros opcionais: o nome de um jogador e a quantidade de gols que ele marcou.
O programa deve ser capaz de mostrar a ficha do jogador, mesmo que algum dos dados não tenha sido informado corretamente."""

'''def ficha(j='', g=''):

    regra = str(g).isnumeric
    if regra == False:
        g = str('0')
    elif j == '':
        j = '<desconhecido>'
    return f'O jogador {j} fez {g} gol(s) no campeonato.'

nome = input('Nome do Jogador: ')
gols = input('Número de Gols: ')

print(ficha(nome, gols))'''

#Guanabara

def ficha(jog = '<desconhecido>', gol = 0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')

n = str(input('Nome do Jogador: '))
g = str(input('Numero de Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)