'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep
n = randint(0,10)
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 10. Tente adivinhar ...')
print('-=-' * 20)
acertou = False
palpite = 0
print('PROCESSANDO...')
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == n:
        acertou = True
    else:
        if jogador < n:
            print('Mais... Tente mais uma vez.')
        elif jogador > n:
            print('Menos... Tente mais uma vez.')
print("Acertou com {} palpites!".format(palpite))