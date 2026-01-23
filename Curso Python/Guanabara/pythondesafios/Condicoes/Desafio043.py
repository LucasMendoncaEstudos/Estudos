'''Desenvolva uyma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5:Abaixo do Peso
-Entre 18.5 e 25:Peso ideal
-25 até 30:Sobrepeso
-30 até 40: Obesidade
-Acima de 40:
Obesidade Mórbida '''
print('Vamos calcular o IMC')
peso = float(input('Qual é seu peso ? (Kg)'))
altura = float(input('Qual é us altura ? (m)'))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if 18.5 < imc:
    print('Você esta Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você esta no Peso Ideal')
elif 25 <= imc < 30:
    print('Você esta no Sobrepeso')
elif 30 <= imc < 40:
    print('Você esta Obeso')
else:
    print('Você esta em Obesidade mórbida')