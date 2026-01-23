


def aumentar(n,x):
    valor = n+(n*(x/100))
    return valor

def diminuir(n,c):
    valor = n - (n*(c/100))
    return valor

def dobro(n) :
    return n *2

def metade(n=0):
    return n/2

'''def moeda(n=0):
    valor = f'R${n :.2f}'.replace('.', ',')
    return valor'''

#guanabara
def moeda(n=0, moeda = 'R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')