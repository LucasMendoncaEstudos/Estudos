'''
Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).

Saída esperada:
Digite seu peso (Kg): 75: 
Digite sua altura (m): 1.68
Seu IMC é: 26.57
Você está acima do peso.
'''

def calculo_imc():
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))
    imc = peso/(altura **2)
    print(f'Seu imc é de {imc:.2f}')
    if imc < 18.5:
        print('Você esta abaixo do peso padrão')
    elif 18.5 <= imc <25:
        print('Você esta no peso padrão.Parabens')
    else:
        print('Você esta acima do peso padrão')
def main():
    calculo_imc()

if __name__=='__main__':
    main()