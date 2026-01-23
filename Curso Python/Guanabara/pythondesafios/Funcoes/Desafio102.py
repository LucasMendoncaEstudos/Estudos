"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro, indicando o número a calcular, e o segundo, chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""

'''def fatorial(num, show = False):
    """Calcula o Fatorial de um número.
    num: O número a ser calculado.
    show: (Opicional) Mostrar ou não a conta.
    return: O valor do Fatorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show == True:
        for c in range(num,0,-1):
            print(f'{c} X', end=' ')
        return f
    else:
        return f

print(fatorial(5,))

help(fatorial)'''

#guanabara:

def fatorial(num, show = False):
    """Calcula o Fatorial de um número.
    num: O número a ser calculado.
    show: (Opicional) Mostrar ou não a conta.
    return: O valor do Fatorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(9, True))