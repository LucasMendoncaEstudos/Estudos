#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar(Considere US$1.00=R$5,53).
n = float(input('Digite quantos reais voce tem para saber quantos dolares pode comprar:'))
n2 = n/5.51
print(f'Com {n :.2f} reais, voce pode comprar {n2 :.2f} dolares.')