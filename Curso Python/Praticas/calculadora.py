def leia_int(msg):
    while True:
        try:
            return int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\nEntrada interrompida pelo usuário.')
            return 0


def ler_operacao():
    while True:
        op = input('Escolha a operação (+, -, *, /, %, H(Historico)): ').strip().upper()
        if op in ['+', '-', '*', '/', '%', 'H']:
            return op
        print('Operação inválida. Tente novamente.')

def mostrar_historico(historico):
        if not historico:
            print('Nenhuma operação realizada ainda')
        else:
            for i, item in enumerate(historico, start=1):
                print (f'{i}) {item}')

def escolhas():
    numero1 = leia_int('Digite o primeiro número: ')
    numero2 = leia_int('Digite o segundo número: ')
    operacao = ler_operacao()
    return numero1, numero2, operacao

def soma(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2 

def porcentagem(numero1, numero2):
    return numero1 * (numero2/100)

def divisao(numero1, numero2):
    if numero2 == 0:
        return None
    return numero1 / numero2 

def continuar():
    while True:
        resposta = input('Quer continuar? [S/N]: ').strip().upper()
        if resposta in ['S', 'N']:
            return resposta == 'S'
        print('Entrada inválida. Digite S ou N.')

operacoes = {
        '+': soma,
        '-': subtrair,
        '*': multiplicar,
        '/': divisao,
        '%': porcentagem,
    }

def main():
    historico = []
    while True:
        numero1, numero2, operacao = escolhas()
        if operacao == 'H':
            mostrar_historico(historico)
            continue
        resultado = operacoes[operacao](numero1, numero2)        
        if resultado is None:
            print('Erro: divisão por zero não é permitida.')
        else:
            print(f'O resultado é {resultado}')
            historico.append(f'{numero1} {operacao} {numero2} = {resultado}')

        if not continuar():
            print('Encerrado.')
            break


if __name__ == '__main__':
    main()