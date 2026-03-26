

'''Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.

Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.

Exemplo de entrada:


Digite um número: 5 
Copiar código
Saída esperada:


A soma de 1 a 5 é: 15 '''

def somar(numero):
    if numero == 1:
        return 1
    return numero + somar(numero - 1)

def main():
    print(somar(5))

if __name__ == '__main__':
    main()