'''4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.'''



def dicionario():
    dicio = {'nome': 'Lucas', 'idade': 24, 'cidade': 'Goiânia'}
    print(dicio)
    if 'nome' in dicio:
        print('A chave "nome" existe no dicionário')
    else:
        print('A chave "Nome" não existe no dicionario')
        

def main():
    dicionario()

if __name__ == '__main__':
    main()