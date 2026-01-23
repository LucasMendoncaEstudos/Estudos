'''Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.'''


def calculo_da_lista():
    lista = [2,6,9,7,2,1,None,'']
    soma = 0
    
    try:
        for i in lista:
            soma += i
        print(f'Soma dos elementos: {soma}')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
def main():
    calculo_da_lista()

if __name__ == '__main__':
    main()