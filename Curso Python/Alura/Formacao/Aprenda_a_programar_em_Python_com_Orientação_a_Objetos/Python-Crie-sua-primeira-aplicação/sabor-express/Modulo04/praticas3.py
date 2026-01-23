'''3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.'''



def dicionario():
    numeros_quadrados = {x : x**2 for x in range(1,6)}
    print(numeros_quadrados)
def main():
    dicionario()

if __name__ == '__main__':
    main()