'''faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamhanho adaptável. 
ex escreva('Ola, Mundo!')
saida:
------------
Ola, Mundo!
------------'''
def escreva(msg):
  tam = len(msg) + 4
  print('~'* tam)
  print(f'   {msg}')
  print('~'* tam)

#Código principal
escreva('Lucas')
escreva('Programador')