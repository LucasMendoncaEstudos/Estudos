#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos quilometros você percorreu ? '))
dias = int(input('Por quantos dias ? '))
total = (dias * 60) + (km * 0.15)
print(f'O total a pagar de {km}Km por {dias} dias é de {total :.2f}R$')