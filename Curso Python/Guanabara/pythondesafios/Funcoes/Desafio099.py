'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep
def maior(*num):
    print('-='*20)
    print('Analisando os valores passados...')
    cont = 0
    for c in num:
        sleep(0.3)
        print(c,end=' ', flush=True)
    print()
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior número informado foi {max(num)}.')

maior(1,4,5,7,3,2,8)
maior(4,1,7,4,9,100)
maior(4,1)
maior(0)

'''Solução guanabara'''
'''
ef maior(*núm):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
'''