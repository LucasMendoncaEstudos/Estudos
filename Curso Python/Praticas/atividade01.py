'''Crie uma função que recebe um número, e faz um contador regressivo a partir dele'''

def contadores(x):
    while x >= 0:
        print(x)
        x -= 1
    print('fim')

contadores(5)
    

#ex1

def dobro(numero):
    return numero *2

print(dobro(5))

#ex2

def maior(a,b):
    if a > b:
        return (f'O numero {a} é maior que {b}')
    elif a < b:
        return (f'O numero {a} é menor que {b}')
    else:
        return 'Os números são iguais'
    
print(maior(2,3))

#ex3

def aprovado(x):
        return x >= 7

def main():
    numero = float(input(('Digite sua Nota:')))
    if aprovado(numero):
        print('Aprovado')
    else:
        print('Reprovado')
main()