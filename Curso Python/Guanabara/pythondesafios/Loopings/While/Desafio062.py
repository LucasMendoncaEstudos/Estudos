'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.'''

print('Gerador de PA !!')
print('-='*10)
n = int(input('Digite o primeiro termo: '))
razao = int(input( 'Digite a razão: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        termo += razao
        cont += 1
        print('{} -> '.format(termo), end='')
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))