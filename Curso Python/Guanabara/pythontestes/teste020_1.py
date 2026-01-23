def dobra(lst):
  pos = 0
  while pos < len(lst):
    lst[pos]*=2
    pos +=1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


'''def contador(*num):
  tam = len(num)
  print(f'Recebi os valores {num} e são ao todo {tam} números')


contador (2,1,7)
contador(8,0)
contador(4,4,7,6,32)
'''
'''def contador(*num):
  for valor in num:
    print(f'{valor} ', end='')
  print('FIM')'''


'''def soma(a,b):
  print(f'A = {a} e B = {b}')
  s = a + b
  print(f'A soma de A + B é igual a {s}')
  
soma(4,5)'''

'''def mensagem(msg):
  print('-'*30)
  print(msg)
  print('-'*30)
 '''


'''def lin():
  print('-'*30)

lin()
print('   CURSO EM VIDEO   ')
lin()
print('   Aprenda Python   ')
lin()
print('   Lucas Mendonça    ')'''