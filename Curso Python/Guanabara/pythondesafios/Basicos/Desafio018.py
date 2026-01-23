#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin,cos,tan,radians
num = float(input('Digite um angulo: '))
seno = sin(radians(num))
print(f'O ângulo de {num}° em SENO é {seno:.2f}.')
cosseno = cos(radians(num))
print(f'O ângulo de {num}° em COSSENO é {cos:.2f}.')
tang = tan(radians(num))
print(f'O ângulo de {num}° na TANGENTE é {tang:.2f}')
