'''Dentro do pacote utilidadesCeV (criado no desafio 111), crie no módulo dado uma função chamada leiaDinheiro().
Essa função deve funcionar de forma semelhante ao input(), mas com validação de dados, aceitando apenas valores que representem dinheiro.'''

from ex112.utilidadescev import dado
from ex112.utilidadescev import moeda

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p,35,22)
