''' Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.'''

from datetime import date
def lista_de_numeros():
    numeros = []
    for i in range(1,11):
        numeros.append(i)
    print(numeros)

def lista_de_nomes():
    nomes = list()
    for i in range(1,5):
        nomes.append(input(f'Digite o {i}° nome: '))
    print(nomes)

def lista_ano():
    anos = []
    anos.append(int(input('Digite o ano em que voce nasceu: ')))
    anos.append(date.today().year)
    print(anos)

def main():
    lista_de_numeros()
    lista_de_nomes()
    lista_ano()
if __name__ == '__main__':
    main()