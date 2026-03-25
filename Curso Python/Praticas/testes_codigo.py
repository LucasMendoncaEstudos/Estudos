def pergunta():
    return int(input('Digite um número para descobrirmos se ele é par ou ímpar: '))


def impar_ou_par(numero):
    return numero % 2 == 0


def mensagem(resultado):
    return 'É par' if resultado else 'É ímpar'


def continuar():
    while True:
        resposta = input('Quer continuar? [S/N]: ').strip().upper()
        if resposta in ['S', 'N']:
            return resposta == 'S'


def main():
    contagem = pares = impares = 0

    while True:
        numero = pergunta()
        contagem += 1

        resultado = impar_ou_par(numero)

        if resultado:
            pares += 1
        else:
            impares += 1

        print(mensagem(resultado))
        print('-' * 20)

        if not continuar():
            print('Programa encerrado.')
            break

    print(f'O número de tentativas foi: {contagem}')
    print(f'Quantidade de pares: {pares}')
    print(f'Quantidade de ímpares: {impares}')


if __name__ == '__main__':
    main()