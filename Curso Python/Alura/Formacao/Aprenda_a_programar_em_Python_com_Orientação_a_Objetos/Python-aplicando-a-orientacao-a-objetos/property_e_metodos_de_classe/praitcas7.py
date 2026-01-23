'''Crie um método de classe para a conta ClienteBanco.'''

'''Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.'''
class ContaBancaria:
    def __init__(self,titular = '',saldo_inicial = 0.0):
        self._titular = titular
        self._saldo_inicial = saldo_inicial
        

class ClienteBanco:
    def __init__(self, nome = '',idade = 0, cpf = '', saldo = 0.0, ativo = False,  ):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._saldo = saldo
        self._ativo = ativo

    @property
    def ativo(self):
        return 'Sim' if self._ativo else 'Não'
    
    def __str__(self):
        return f'Dados:\nNome:{self._nome}\nIdade:{self._idade}\nCPF:{self._cpf}\nSaldo:{self._saldo:.2f}\nAtivo:{self.ativo}'
    @classmethod
    def criar_conta(cls,titular,saldo_inicial):
        conta = (ContaBancaria(titular,saldo_inicial))
        return conta
    
conta_cliente1 = ClienteBanco.criar_conta('Ana',2000)
    
    
pessoa1 = ClienteBanco('Lucas', 25,'063.228.261-40', 256.12,True)
pessoa2 = ClienteBanco('Fernanda',40,'742.562.144-20',1000,False)
pessoa3 = ClienteBanco('Pedro',32,'462.125.941-80', 2348512.50, True)

print(pessoa1)
print(pessoa2)
print(pessoa3)
print(vars(conta_cliente1))