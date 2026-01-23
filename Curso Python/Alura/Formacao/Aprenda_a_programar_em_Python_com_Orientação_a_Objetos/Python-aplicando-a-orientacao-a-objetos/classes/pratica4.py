'''Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.'''

class Restaurante:
    nome = ''
    categoria = ''
    ativo = True

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
restaurante_pizza = Restaurante()

categoria = Restaurante.categoria 
