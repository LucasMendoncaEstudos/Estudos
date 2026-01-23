
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'

restaurante_pizza = Restaurante()


restaurantes = [restaurante_pizza, restaurante_praca]
print(restaurantes)