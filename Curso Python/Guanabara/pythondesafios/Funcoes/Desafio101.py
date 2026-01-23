"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

'''def voto():
    from datetime import date
    n = int(input('Em que ano voce nasceu ?'))
    idade = date.today().year - n
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')
    elif 18 <= idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    else:
        print(f'Com {idade} anos: O VOTO É OPICIONAL')
voto()'''

#guanabara:

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPICIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    
nasc = int(input('Em que ano você nasceu ? : '))
print(voto(nasc))