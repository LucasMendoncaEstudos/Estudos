'''Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.'''


class Restaurante:

    def __init__(self,nome,categoria, capacidade ,nota_avaliacao,ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        
restaurante_praca = Restaurante('Praça','Goumert', True, 556, 4.5)




