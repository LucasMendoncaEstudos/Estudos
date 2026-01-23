'''Modifique as funções criadas no desafio 107 para que recebam um parâmetro opcional que indique se o valor retornado deve ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''


from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,False)}')#para mostrar a diferença
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando 10% de {moeda.moeda(p)} é {moeda.aumentar(p,10,True)}') 
print(f'Diminuindo 13% de {moeda.moeda(p)} é {moeda.diminuir(p,13,True)}')
