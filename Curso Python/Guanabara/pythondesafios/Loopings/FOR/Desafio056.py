'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.'''

soma = 0
media_i = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher_20 = 0
for pessoas in range(1,5):
    print('-- {}° PESSOA --'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if pessoas == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1

media_i = soma / 4
print('A média da idade do grupo é de {} anos'.format(media_i))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total_mulher_20))