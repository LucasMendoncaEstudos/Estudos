#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.(adicionando todas as medidas)
n = float(input('Digite um numero em metros para descobrir quanto ele vale em centimetros e milímetros:'))
dm = n * 10
cm = n * 100
mm = n * 1000
dam = n / 10
hm = n / 100
km = n / 1000

print(f'{n} metros em todas as medidas são: \nEm decimetro é igual a {dm} \nEm centimetros é igual a {cm}.\nEm milímetros é igual a {mm}\nEm decâmetro é igual a {dam}\nEm hectômetro é igual a {hm}\nEm quilômetro é igual a {km} ')