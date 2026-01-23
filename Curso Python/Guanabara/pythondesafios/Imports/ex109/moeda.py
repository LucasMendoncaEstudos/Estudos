
#fazendo o if ja dentro do return, 3 formas de fazer 
def aumentar(n,x,f=False):
    valor = n+(n*(x/100))
    if f:
        return moeda(valor)
    return valor

def diminuir(n,c,f=False):
    valor = n - (n*(c/100))
    return valor if not f else moeda(valor)

def dobro(n, f = False) :
    valor = n *2
    return valor if f is False else moeda(valor)

def metade(n=0,f = False):
    valor = n/2
    if f:
        return moeda(valor)
    return valor

def moeda(n=0, moeda = 'R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')