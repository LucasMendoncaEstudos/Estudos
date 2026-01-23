'''Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.'''


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

pessoa1 = ContaBancaria('Lucas', 275)
pessoa2 = ContaBancaria('Maria', 9000.24)
ContaBancaria.ativar_conta(pessoa1)
print(pessoa1)
print(pessoa2)