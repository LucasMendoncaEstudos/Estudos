'''Crie um programa que leia o nome completo de uma pessoa e mostre:
*O nome com todas as letras maiúscula.
*O nome com todas minúsculas.
*Quantas letras ao todo (sem considerar espaços).
*Quantas letras tem o primeiro nome.'''
nome = str(input('Digite seu nome completo: ')).strip()
n4 = nome.split()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome  é {} e tem ao todo {} letras'.format(n4[0], len(n4[0])))