'''Praticas de modularização'''

from uteis import numeros #importando pacotes dentro de modulos
''' pode utilizar "from uteis import fatorial , dobro" ( ai não precisa colocar o uteis antes, mas não é recomendado, o melhor é utilizar o primeiro)'''

num = int(input("Digiteum valor: "))
fat = numeros.fatorial(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')