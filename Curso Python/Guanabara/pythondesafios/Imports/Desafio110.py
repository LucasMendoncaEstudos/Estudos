'''Adicione ao módulo moeda.py (criado nos desafios anteriores) uma função chamada resumo().
Essa função deve exibir na tela um relatório resumido, com algumas informações geradas pelas funções já existentes no módulo, como aumento, redução, dobro e metade do valor informado.'''
from ex110 import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 80, 35)

