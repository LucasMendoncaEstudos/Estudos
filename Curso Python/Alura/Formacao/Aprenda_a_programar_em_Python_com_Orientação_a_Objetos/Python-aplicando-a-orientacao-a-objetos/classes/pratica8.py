'''Mude o estado da instância restaurante_pizza para ativo.'''


class Restaurante:
    nome = ''
    categoria = ''
    ativo = True

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

print(restaurante_pizza.ativo)