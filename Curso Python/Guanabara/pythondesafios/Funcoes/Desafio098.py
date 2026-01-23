'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada: 
A)De 1 até 10, de 1 em 1.
B)De 10 até 0, de 2 em 2.
C)Uma contagem personalizada '''

from time import sleep
'''Minha tentativa:
 def contador(i,f,p):
    print('-=' * 10)
    print('Contagem de 1 até 10 de 1 em 1')
    inicio = fim = passo = 0
    for c in range(1, 11, 1):
        print(c, end=' ')
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10, -2, -2):
        print(c, end=' ')
    print('Agora vamos personalizar')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(c)
    elif inicio > fim:
        for c in range(inicio, fim, -passo):
            print(c)
    elif passo < 0:
        for c in range(inicio, fim, -passo):
            print(c)'''

def contador(i,f,p):
    if p < 0 :
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    
    if i < f:
        cont = i
        while cont <= f:
            sleep(0.3)
            print(f'{cont} ', end='', flush=True)
            cont += p
        print(' Fim!')
    else:
        cont = i
        while cont >= f:
            sleep(0.3)
            print(f'{cont} ', end='', flush=True)
            cont -= p
        print(' Fim!')
    
#programa principal
contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)