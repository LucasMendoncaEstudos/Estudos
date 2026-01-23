'''2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.'''


def dicionario():
    dicio = {'nome': 'Lucas', 'idade': 24, 'cidade': 'Goiânia'}
    print(dicio)
    print(f'Alterando a idade para 27 anos e adicionando profissão')
    dicio['idade'] = 27
    dicio['profissao'] = 'Desenvolvedor'
    print(dicio)
    del dicio['cidade']
    print(dicio)

def main():
    dicionario()

if __name__ == '__main__':
    main()