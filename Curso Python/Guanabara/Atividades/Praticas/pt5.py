'''Práticas de Definição'''

'''def mostraLinha():
    print('-'*30)


mostraLinha()
print('Curso em video')
mostraLinha()
print('Aprenda python')
mostraLinha()'''

'''def soma (a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

soma(5,8)'''

'''def contador(*num):
    for valor in num:
        print(f'{valor}', end=' ')

contador(2,1,7)
contador(9,7,2)
contador(1,5,8)'''



def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos +=1
valores = [5,2,8,1,5,3]
dobra(valores)
print(valores)