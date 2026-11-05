'''Faça um porgrama que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''





lista = []

for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))

maximo = max(lista)
minimo = min(lista)

for indice, valor in enumerate(lista):
    if valor == maximo:
        print(f'O maior valor digitado foi {maximo} na posição {indice}')
    if valor == minimo:
        print(f'O menor valor digitado foi {minimo} na posição {indice}')




































"""listanum = []
mai = 0
men = 0
for c in range(0,5):
  listanum.append(int(input(f'Digite um valor para a Posição {c}:')))
  if c == 0:
    mai = men = listanum[c]
  else:
    if listanum[c] > mai:
      mai = listanum[c]
    if listanum[c] < men:
       men = listanum[c]
print('=-'*30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i,v in enumerate(listanum):
  if v == mai:
    print(f'{i}... ')
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i,v in enumerate(listanum):
  if v == men:
    print(f'{i}...', end='')"""