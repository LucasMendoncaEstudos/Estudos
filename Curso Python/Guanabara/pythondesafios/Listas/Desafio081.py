'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A)Quantos números foram digitados.
B)Alista de valores, ordenada de forma decrescente.
C)Se o valor 5 foi digitado e está ou não na lista.'''

lista = list()
cont = 0
while True:
  n = (int(input('Digite um valor: ')))
  lista.append(n)
  print('Valor adicionado com sucesso!')
  cont += 1
  resposta = str(input('Quer continuar? [S/N] :')).strip().upper()[0]
  if resposta == 'N':
    break
    
print(f'Foram digitados {cont} números')
#ou pode usar o len q fica print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica {lista}')
if 5 in lista:
    print('Existe o valor 5 na lista')
else:
  print('Não existe o valor 5 na lista')
