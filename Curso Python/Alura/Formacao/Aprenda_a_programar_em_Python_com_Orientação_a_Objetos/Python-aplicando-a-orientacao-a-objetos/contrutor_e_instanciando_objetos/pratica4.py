'''Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.'''

class Restaurante:

    def __init__(self,nome,categoria, capacidade ,nota_avaliacao,ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
        
restaurante_praca = Restaurante('Praça','Goumert', True, 556, 4.5)

print(restaurante_praca)