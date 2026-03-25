'''Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.

Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().'''
def valores_pares():
    valores = input("Digite os numeros separados por espaço: ").split()
    itens = filter(lambda x: int(x) % 2 == 0, valores)
    return list(itens)

def main():
    pares = valores_pares()
    print("Números pares:", " ".join(map(str, pares)))

if __name__ == '__main__':
    main()