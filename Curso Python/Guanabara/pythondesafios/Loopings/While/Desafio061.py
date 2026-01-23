'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('Gerador de PA !!')
print('-='*10)
n = int(input('Digite o primeiro termo: '))
razao = int(input( 'Digite a razão: '))
termo = n
cont = 1
while cont <= 10:
    termo += razao
    cont += 1
    print('{} -> '.format(termo), end='')
print('FIM')


