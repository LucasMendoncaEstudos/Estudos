'''
Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

O valor da renda mensal precisa ser maior que R$ 2.000,00.
O valor da parcela não pode ultrapassar 30% da renda.
Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.

Saída esperada:
Digite o valor da sua renda mensal: 2500
Digite o valor da parcela desejada: 800
Empréstimo negado: parcela acima de 30%
'''
def parcelas():
    renda = float(input('Digite o valor da sua renda mensal: '))
    parcela = float(input('Digite o valor da parcela desejada: '))
    if renda > 2000 and parcela <= 0.3 * renda:
        print("Empréstimo aprovado!")
    elif renda <= 2000:
        print("Empréstimo negado: renda insuficiente.")
    else:
        print('Empréstimo negado: parcela acima de "30%" da renda.')


def main():
    parcelas()

if __name__ == '__main__':
    main()