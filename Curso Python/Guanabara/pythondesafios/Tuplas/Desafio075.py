'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A)Quantas vezes apareceu o valor 9.
B)Em que posição foi digitado o primeiro valor 3.
C)Quais foram os número pares.'''

valores = (int(input('Digite o primeiro valor :')), int(input('Digite o segundo valor: ')), int(input('Digite o terceiro valor: ')), int(input('Digite o ultimo valor: ')))


print(f'Seus valores digitados foram: {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O número 3 aparece primeiro na {valores.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares foram :', end='')
for n in valores:
    if n % 2 ==0:
        print(n,end=' ')