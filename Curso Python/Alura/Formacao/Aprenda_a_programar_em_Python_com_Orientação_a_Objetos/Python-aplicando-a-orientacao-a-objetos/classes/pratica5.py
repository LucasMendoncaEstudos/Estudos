'''Altere o valor do atributo nome para 'Bistrô'.'''

class Restaurante:
    nome = ''
    categoria = ''
    ativo = True

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
restaurante_pizza = Restaurante()

restaurante_praca.nome = 'Bistrô'

