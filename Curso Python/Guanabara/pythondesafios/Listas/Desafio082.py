'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

lista = list()
par = list()
impar = list()
while True:
  lista.append(int(input('Digite um valor: ')))
  resposta = (str(input('Quer continuar ? [S/N]:'))).strip().upper()[0]
  if resposta == 'N':
    break
for i, v in enumerate(lista):
  if v % 2==0:
    par.append(v)
  else:
    impar.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}!')
print(f'A lista de impares é {impar}!')