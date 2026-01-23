'''Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
o programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep #Função que para o processamento
n = randint(0,5) # Pega um numero aleatorio de 0 ate 5.
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5. Tente adivinhar ...')
print('-=-' * 20)
numero = int(input('Em que numero eu pensei ?: '))#buscando a resposta do usuario.
print('PROCESSANDO...')
sleep(3)
if numero == n: 
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(n,numero))


