'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem,cobrando R$0,50 por Km para viagens de até
200Km e R$0,45 para viagens mais longas.'''

viagem = float(input('Qual é a distância da sua viagem ? '))
print('Você esta prestes a começar sua viagem de {:.2f}Km.'.format(viagem))
if viagem <= 200:
    valor = viagem * 0.50
else:
    valor = viagem * 0.45
print('E o preço da sua passagem será de {} R$'.format(valor))


