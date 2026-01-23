'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

soma = media = cont = maior = menor = 0 
resposta = 'S'
while resposta in 'sS':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
media = soma/cont
print('Voce digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))

