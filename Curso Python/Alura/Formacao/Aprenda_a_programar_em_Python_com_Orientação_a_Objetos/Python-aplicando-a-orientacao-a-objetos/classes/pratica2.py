'''Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.'''
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
restaurante_pizza = Restaurante()


restaurantes = [restaurante_pizza, restaurante_praca]
print(restaurante_praca.nome)
#ou
nome_do_restaurante = restaurante_praca.nome
print(nome_do_restaurante)
