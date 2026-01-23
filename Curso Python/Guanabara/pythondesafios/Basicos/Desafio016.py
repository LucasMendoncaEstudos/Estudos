#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. ex:Digite um número:6.127. O numero 6.127 tem a parte inteira 6.
from math import trunc
num = float(input('Digite um numero real qualquer: '))
print(f'O número {num} tem sua porção inteira de {trunc(num)}')
