'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.'''

def area(l,c):
  area = l * c
  print(f'A área de um terreno {l}x{c} é de {area}m2')

#codigo principal

print(' Controle de terrenos ')
print('-'*20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)