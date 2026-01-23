#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m**2.
n = float(input('Digite a largura de sua parede em metros:'))
n2 = float(input('Digite a altura de sua parede em metros:'))
a = n * n2
print(f'Sua parede tem a dimensão de {n}x{n2} e sua área é de {a}m2.')
t = a / 2
print(f'Para pintar essa parede, você precisará de {t}l de tinta')

