'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.'''
totgasto = 0
maiorM = 0
menor = 0
cont = 0
barato = ''
while True:
    nome = str(input('Digite o nome do seu produto: '))
    preco = float(input('Digite o preço do seu produto: '))
    totgasto += preco
    cont += 1

    if preco > 1000:
        maiorM += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format('Fim do Programa'))
print(f'O total gasto na compra foi de R${totgasto:.2f}')
print(f'Temos {maiorM} produtos custando mais de 1000.00 reais')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

