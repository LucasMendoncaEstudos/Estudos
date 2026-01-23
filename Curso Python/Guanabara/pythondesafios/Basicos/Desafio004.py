#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.
print ('Vamos descobrir o que você digitou ?')
n = input('Digite algo = ')
print('O que voce digitou é um(a)', type(n))
print('Só tem espaços ? ', n.isspace())
print('É um número ? ', n.isnumeric())
print('É alfabético ? ', n.isalpha())
print('É alfanumérico ?', n.isalnum())
print('Está em maiúsculas ?', n.isupper())
print('Está em minúsculas ?', n.islower())
print('Esta capitalizada ?', n.istitle()) #quer dizer que tem o maiúsculo e minúsculo
