'''Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.'''



def calculo_da_media():
    numeros = [10,2,123]
    soma = 0
    try:
        for i in numeros:
            soma += i
        media = soma/len(numeros)
        print(f'A média é {media}')
    except ZeroDivisionError:
        print('A lista esta vazia, não é possivel calcular a média')
    except Exception as e:
        print(f'Error{e}')

def main():
    calculo_da_media()

if __name__ == '__main__':
    main()