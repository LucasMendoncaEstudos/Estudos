'''Crie um pacote chamado utilidadesCeV, contendo dois módulos internos:

moeda

dado

Transfira todas as funções criadas nos desafios 107, 108 e 109 para dentro do módulo moeda, mantendo tudo funcionando.'''

from ex111.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p,35,22)