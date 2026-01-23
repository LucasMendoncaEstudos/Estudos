'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguas'''
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O número {} é maior que o número {}'.format(n1,n2))
elif n2 > n1:
    print('O número {} é maior que o número {}'.format(n2,n1))
else:
    print('Não existe valor maior os números {} e {}, são iguais!'.format(n1,n2))