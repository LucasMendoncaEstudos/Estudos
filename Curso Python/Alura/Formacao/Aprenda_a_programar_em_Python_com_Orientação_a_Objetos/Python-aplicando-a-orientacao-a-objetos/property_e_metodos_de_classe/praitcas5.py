'''Crie uma instância da classe e imprima o valor da propriedade titular.'''

class ContaBancaria:
    def __init__(self, titular = '',saldo=float):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
    def __str__(self):
        return f'O titular da conta é {self.titular} | Saldo: {self.saldo:.2f} | Conta Ativa : {self.ativo}'
    @classmethod
    def ativar_conta(cls):
        cls.ativo = True

pessoa1 = ContaBancaria('Fernanda', 25)
print(pessoa1.titular)