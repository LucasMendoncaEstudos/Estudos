'''
Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

Saída esperada:
Informe os dias para a atividade A: 
Informe os dias para a atividade B: 
Informe os dias para a atividade C: 
Erro: Os dias não podem ser negativos.
'''
def tempo():
    a = int(input('Informe os dias para a atividade A: '))
    b = int(input('Informe os dias para a atividade B: '))
    c = int(input('Informe os dias para a atividade C: '))
    if a < 0 or b < 0 or c < 0:
        print('Erro: Os dias não podem ser negativos.')
    else:
        soma = a+b+c
        print(f'O total de dias para fazer o projeto foram de {soma}')

def main():
    tempo()

if __name__=='__main__':
    main()