'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.No final, mostre:
A)Quantas pessoas foram cadastradas.
B)Uma listagem com as pessoas mais pesadas.
C)Uma listagem com as pessoas mais leves.'''

dados = list()
lista = list()
mai = men = 0
while True:

    dados.append(str(input('Digite um nome: ')))
    dados.append(float(input('Digite um peso: (kg)')))
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()

    resposta = (str(input('Quer continuar ? [S/N]'))).strip().upper()
    if resposta == 'N':
        break
print(f'A quantidade de pessoas cadastradas é de: {len(lista)} pessoas')
print(f'O maior peso foi de {mai}Kg. peso de ', end='')
for p in lista:
    if p[1] == mai:
        print(f'{p[0]} ', end ='')
print(f'O menor peso foi de {men}Kg.Peso de ',end='')
for p in lista:
    if p[1] == men:
        print(f'{p[0]} ', end='')
