'''Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade 
 e quantas já são maiores.(considere maioridade com 21 anos)'''
from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade < 21:
        totmenor += 1
    else:
        totmaior += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E tambem tivemos {} pessoas menores de idade.'.format(totmenor))

