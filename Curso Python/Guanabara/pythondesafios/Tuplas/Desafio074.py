'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e tambem indique o menor e o maior valor que estão na tupla'''
from random import randint
from traceback import print_tb
maior = 0
menor = 0
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Eu sorteei os valores {n}')
print(f'O maior número sorteado foi {max(n)}')
print(f'O menor número sorteado foi {min(n)}')
