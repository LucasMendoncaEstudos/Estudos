'''Pratica de dicionarios'''

'''pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Marcos'
pessoas['peso'] = '98.5'

for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = []
estado1 = {'uf': 'Brasília', 'sigla':'DF'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'A chave {k} tem {v}')