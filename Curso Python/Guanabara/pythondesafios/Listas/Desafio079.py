'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

lista = []
while True:
  n = (int(input('Digite um valor:')))
  if n not in lista:
    lista.append(n)
    print('Valor adicionado com sucesso!')
  else:
    print('Valor repetido! Não pode ser adicionado')
  resposta = str(input('Quer continuar ? [S/N]:')).strip().upper()[0]
  if resposta == 'N':
      break
lista.sort()
print(f'Você digitou os valores {lista}')