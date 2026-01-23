'''Reescreva a função leiaInt() feita no desafio 104, incluindo agora a possibilidade de tratamento para quando o usuário digitar um valor inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido. \033[m')
            continue
        except(KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número real válido. \033[m')
            continue
        except(KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n

n = leiaInt('Digite um Inteiro ')
s = leiaFloat('Digite um Real: ')
print(f'Voce acabou de digitar o número {n} e {s}')