'''Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.'''



def numeros_decrescente():
    for i in range(10,0,-1):
        print(i)

def main():
    numeros_decrescente()

if __name__ == '__main__':
    main()