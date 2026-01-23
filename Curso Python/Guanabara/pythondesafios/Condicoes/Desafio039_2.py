'''Codigo um pouco melhorado do desafio 39 '''
from datetime import date


def calcula_idade(ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento
    return idade


def mostra_resultado(idade, nasceu, atual):
    if idade < 18:
        print(
            f'Quem nasceu em {nasceu}, tem {idade} anos de idade em {atual}.')
        print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
        print('Seu alistamento será em {}.'.format((18-idade) + atual))
    elif idade > 18:
        print(
            f'Quem nasceu em {nasceu}, tem {idade} anos de idade em {atual}.')
        print('Você ja deveria ter se alistado há {} anos'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(atual - (idade - 18)))
    else:
        print(
            f'Quem nasceu em {nasceu}, tem {idade} anos de idade em {atual}.')
        print('Você tem que se alistar IMEDIATAMENTE!')


print('Vamos descobrir quando você precisa se alistar no exercito')
m = int(input('''Você é homem ou mulher?
[1] para Mulher
[2] para Homem
Resposta: '''))

while True:
    try:
        if m == 1:
            ano_atual = date.today().year
            ano_nascimento = int(input('Em que ano você nasceu?:'))
            idade_homem = calcula_idade(ano_atual, ano_nascimento)
            mostra_resultado(idade_homem, ano_nascimento, ano_atual)
            break
        elif m == 2:
            ano_atual = date.today().year
            ano_nascimento = int(input('Em que ano você nasceu?:'))
            idade_mulher = calcula_idade(ano_atual, ano_nascimento)
            mostra_resultado(idade_mulher, ano_nascimento, ano_atual)
            break
    except ValueError:
        print('Valor digitado incorreto, apenas números')
        continue
    except Exception as E:
        print(E.__class__)
        print(E)
