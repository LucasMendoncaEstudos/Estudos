#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o valor de seu salário: '))
novo_salario = salario + (salario * 15/100)
print(f'Seu salario de {salario :.2f} R$ com 15% de aumento fica {novo_salario:.2f} R$')