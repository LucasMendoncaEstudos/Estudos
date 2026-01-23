'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A)Quantas pessoas foram cadastradas
B)A média de idade do grupo.
C)Uma lista com todas as mulheres.
D)Uma lista com todas as pessoas com idade acima da média.'''

dados = dict()
pessoas = list()
soma = media = 0
while True:
  dados.clear()
  dados['nome'] = str(input('Nome: '))
  while True:
    dados['sexo'] = str(input('Sexo: [M/F]').strip().upper()[0])
    if dados['sexo'] in 'MF':
      break
    print('ERRO! Por favor, digite apenas M ou F.')
  dados['idade'] = int(input('Idade: '))
  soma += dados['idade']
  pessoas.append(dados.copy())
  while True:
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resposta in 'SN':
        break
    print('ERRO" Por favor, digite apenas S ou N.')
  if resposta == 'N':
    break

print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'B) A média de idade é de {media: 5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in pessoas:
  if p['sexo'] in 'F':
    print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in pessoas:
  if p['idade'] >= media:
    for k, v in p.items():
      print(f'{k} = {v}; ', end='')
      print()
print('<< ENCERRADO >>')