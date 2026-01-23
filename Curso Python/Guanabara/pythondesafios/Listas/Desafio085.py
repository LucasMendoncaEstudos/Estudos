'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.No final, montre os valores pares e ímpares em ordem crescente.'''
dados = [[], []]
lista = 0
for c in range(1,8):
    valor = (int(input(f'Digite o {c}. valor: ')))
    if valor % 2==0:
        dados[0].append(valor)
    else:
        dados[1].append(valor)
dados[0].sort()
dados[1].sort()
print(f'Os valores pares digitados foram: {dados[0]}')
print(f'Os valores ímpares digitados foram: {dados[1]}')