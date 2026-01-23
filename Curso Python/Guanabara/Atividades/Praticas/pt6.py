'''def fatorial(num=1):
    """
    Def para fatoriais
    """
    f = 1
    for c in range(num, 0, -1):
        f*=c
    return f 

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
help(fatorial)
'''

def parOuImpar(n=0):
    if n% 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if parOuImpar(num):
    print('É par')
else:
    print('É ímpar')
