'''Imprima no console o nome e a categoria da instância restaurante_praca.'''

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

print(vars(restaurante_praca))
#ou 
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')