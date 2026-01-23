'''Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.'''


class ContaBancaria:
    def __init__(self, titular = '',saldo=float):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

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