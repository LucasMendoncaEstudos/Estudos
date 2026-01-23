'''
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

Saída esperada:
Digite o total de despesas do mês (R$): 
Atenção! Você ultrapassou o limite do orçamento.

'''

def orcamento():
    limite = 3000
    despesas = float(input('Digite o total de despesas do mês R$:'))

    if despesas > limite:
        print('Atenção! Voce ultrapassou o limite do orçamento')
    elif despesas == limite:
        print('Voce gastou o limite máximo e não possui mais nada')
    else:
        print(f'Voce ainda esta dentro do limite, ainda possui R${limite - despesas:.2f}')

def main():
    orcamento()

if __name__=='__main__':
    main()