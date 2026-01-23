'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluido o total de gols feitos durante o campeonato.'''

dados = dict()
partidas = list()
dados['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
if partidas !=0:
  for k in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {k+1}? ')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print('-='*30)
print(dados)
print('-='*30)
for c, v in dados.items():
  print(f'O campo {c} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {tot} partidas')
for i,v in enumerate(dados['gols'], start=1):
  print(f'  => Na partida {i}, fez {v} gols')
print(f'Foi um total de {dados["total"]} gols')
