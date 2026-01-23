'''Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.'''

class Restaurante:
    nome = ''
    categoria = ''
    ativo = True

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'
restaurante_pizza = Restaurante()

if restaurante_praca.ativo == True:
    print('O restaurante esta ativo')
else:
    print('O restaurante esta inativo')