'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''
lista = list()
for c in range(0,5):
  d = int(input('Digite um valor: '))
  if c == 0 or d > lista[-1] :
    lista.append(d)
  else:
    pos = 0
    while pos <len(lista):
      if d <= lista[pos]:
        lista.insert(pos,d)
        break
      pos +=1

print(f'Os valores digitados em ordem foram {lista}')