'''
Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
'''
def numero():
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        print('Seu número é par!')
    else:
        print('Seu número é impar')

def main():
    numero()
if __name__ == '__main__':
    main()