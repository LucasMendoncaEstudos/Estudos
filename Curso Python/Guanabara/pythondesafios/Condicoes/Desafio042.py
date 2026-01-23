'''Refaça o DESAFIO 035 dos triãngulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
-Equilátero: todaos os lados iguais
-Isóceles:dois lados iguais
-Escaleno: todos os lados diferentes'''
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM formar um triângulo')
    if n1 == n2 == n3:
        print('Formara um triângulo EQUILÁTERO (todos os lados iguais)')
    elif n1 != n2 != n3 != n1:
        print('Formara um triângulo ESCALENO (todos os lados diferentes)')
    else:
        print('Formara um triângulo ISÓCELES (dois lados iguais)')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')