'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

n = 1
while True:
    n = int(input('Digite um número para vermos sua tabuada: '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(n, c, n*c))
    print('-' * 30)
print('Programa de tabuado ecenrrado !!')