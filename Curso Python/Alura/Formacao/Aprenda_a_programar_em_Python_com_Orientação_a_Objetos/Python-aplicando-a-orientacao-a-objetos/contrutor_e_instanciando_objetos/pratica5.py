'''Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.'''

class Cliente:
    def __init__(self, nome,idade,sexo,ativo = False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.ativo = ativo
    
cliente_ativo = Cliente('Lucas', 25, 'M', True)
cliente_ativo = Cliente('Maria', 24, 'F', False)
cliente_ativo = Cliente(nome='Gustavo', idade=20, sexo='M')
        