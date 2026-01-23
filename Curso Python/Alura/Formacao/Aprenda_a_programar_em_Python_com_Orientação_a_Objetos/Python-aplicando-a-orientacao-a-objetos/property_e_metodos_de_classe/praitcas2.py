'''Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.'''


class ContaBancaria:
    def __init__(self, titular = '',saldo=float):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f'O titular da conta é {self.titular} | Saldo: {self.saldo:.2f}'

pessoa1 = ContaBancaria('Lucas', 275)
pessoa2 = ContaBancaria('Maria', 9000.24)

print(pessoa1)
print(pessoa2)