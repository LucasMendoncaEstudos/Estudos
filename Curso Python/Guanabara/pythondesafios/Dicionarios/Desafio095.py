'''Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
dados = dict()
partidas = list()
time = list()
while True:
  dados.clear()
  dados['nome'] = str(input('Nome do Jogador: '))
  tot = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
  partidas.clear()
  if partidas !=0:
    for k in range(0,tot):
      partidas.append(int(input(f'Quantos gols na partida {k+1}? ')))
  dados['gols'] = partidas[:]
  dados['total'] = sum(partidas)
  time.append(dados.copy())
  while True:
    resposta = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if resposta in 'SN':
      break
    print('Erro! Digite apenas S ou N')
  if resposta == 'N':
    break
print('-'*40)
print('cod ', end='')
for i in dados.keys():
  print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
  print(f'{k:>3} ', end='')
  for d in v.values():
    print(f'{str(d):<15}', end='')
  print()
print('-'*40)
while True:
  busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
  if busca == 999:
    break
  if busca >=len(time):
    print(f'ERRO! Não existe jogador com código {busca}!')
  else:
    print(f' -- LEVANTAMENT0 DO JOGADOR {time[busca] ["nome"]}:')
    for i, g in enumerate(time[busca]['gols']):
      print(f'  No jogo {i+1} fez {g} gols')
  print('-'*40)
print('<<VOLTE SEMPRE>>')
