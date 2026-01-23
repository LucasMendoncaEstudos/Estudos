'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''

tot18 = 0
masc = 0
fem = 0

while True:
    idade = int(input("Digite sua idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:[M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        fem += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de Homens cadastrados é de {masc}')
print(f'Total de mulheres que tem menos de 20 anos é de {fem}')
print('FIM')
