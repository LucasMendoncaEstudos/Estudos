'''Adapte o código do desafio 107, criando uma função adicional chamada moeda() que seja capaz de exibir os valores já formatados como valores monetários.'''

from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)} é {moeda.aumentar(p,10)}') #para mostrar a diferença
print(f'Diminuindo 13% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p,13))}')
