estado = dict()
brasil = list()
for c in range(0,3):
  estado['uf'] = str(input('Unidade Federativa: '))
  estado['sigla'] = str(input('Sigla do Estado: '))
  brasil.append(estado.copy())
for e in brasil:
  for k, v in e.items():
    print(f'O campo {k} tem valor {v}.')

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

#print(brasil[0]['uf']) aqui vai pegar o primeiro dicionario e mostrar o uf do primeiro que é Rio de janeiro
#print(brasil[0]) aqui ira aparecer o primeiro dicionario adicionado
#print(brasil)'''