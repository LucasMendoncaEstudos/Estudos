'''Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.

Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.'''

def contador(texto):
    return len(texto)

def main():
    palavra = input('Digite uma palavra: ')
    print(f'Essa palavra tem {contador(palavra)} caracteres')

if __name__ == '__main__':
    main()