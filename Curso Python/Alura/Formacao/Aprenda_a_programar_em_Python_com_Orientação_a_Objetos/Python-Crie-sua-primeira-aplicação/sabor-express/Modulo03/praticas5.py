'''Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.'''



def tabuada():
    numero = int(input('Digite um número para mostrar sua tabuada: '))

    for i in range(1,11):
        print(f'{numero} X {i} = {i*numero}')

def main():
    tabuada()

if __name__ == '__main__':
    main()