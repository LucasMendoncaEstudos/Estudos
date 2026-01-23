valores = list()
for cont in range(0, 5):
  valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
  print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')








'''valores = []
valores.append(4)
valores.append(0)
valores.append(0)

for c, v in enumerate(valores):
  print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

'''
num = [3,2,1,8,1,8,1]
num[2] = 4
num.append(9)
num.sort(reverse=True)
num.insert(4,0)
num.pop()
if 3 in num:
  num.remove(3)
else:
  print('Não tem este elemento na lista')
print(num)
print(f'Essa lista tem {len(num)} elementos')'''