'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

n = []
while True:
  nome = str(input('Nome: '))
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  media = (nota1 + nota2) / 2
  n.append([nome, [nota1, nota2], media])
  resposta = str(input('Quer continuar ? [S/N]:')).strip().upper()[0]
  if resposta == 'N':
    break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(n):
  print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
  print('-'*35)
  opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

  if opc == 999:
    print('FINALIZANDO...')
    break
  if opc<= len(n) -1:
    print(f'Notas de {n[opc][0]} são {n[opc][1]}')