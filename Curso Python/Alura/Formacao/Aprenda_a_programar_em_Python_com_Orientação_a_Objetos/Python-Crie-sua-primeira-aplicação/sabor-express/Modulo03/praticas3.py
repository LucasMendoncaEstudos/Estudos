'''Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.'''


def calculo_da_soma():
    soma = []
    for i in range(1,11):
        if i % 2 == 0:
            pass
        else:
            soma.append(i)
    soma_total = sum(soma)
    print(soma_total)



def main():
    calculo_da_soma()
if __name__ == '__main__':
    main()


'''Versão Alura :
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)
'''