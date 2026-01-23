'''Escreva um programa que leia um número inteiro qualquer e peça para
 o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal'''
numero = int(input('Digite um número inteiro: '))
tipo = int(input('Agora digite o número de escolha para mostrar em \n1-Binário\n2-Octal\n3-Hexadecimal\nSua opção: '))
if tipo == 1:
    print('O número {} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif tipo == 2:
    print('O número {} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif tipo == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção Inválida, tente novamente')
