'''Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.'''


class Restaurante:

    def __init__(self,nome,categoria, capacidade ,nota_avaliacao,ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        
restaurante_praca = Restaurante('Praça','Goumert', True, 556, 4.5)
novo_restaurante = Restaurante(nome='Santa Marmita', categoria='Fast Food')
