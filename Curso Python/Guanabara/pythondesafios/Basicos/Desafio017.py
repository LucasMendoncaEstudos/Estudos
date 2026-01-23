#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
print(f'O valor da hipotenusa é de {hypot(co,ca):.2f}')