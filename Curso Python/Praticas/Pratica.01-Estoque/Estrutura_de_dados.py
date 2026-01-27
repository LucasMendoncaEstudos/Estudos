import os

dados = {"arroz": {"preco": 20.5, "quantidade": 10},
         "feijão": {"preco": 8.9, "quantidade": 5}}


def exibir_nome_do_programa():
    print("Controle de estoque")

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_produto():
    for i in range(2):
        exibir_subtitulo('Cadastro de Novos Produtos')
        nome_do_produto = input('Digite o nome do produto:')
        preco_do_produto = float(input('Digite o preço deste produto R$:'))
        quantidade_do_produto = int(input('Digite a quantidade deste produto em Unidades:'))

        if nome_do_produto in dados:
            print('Produto ja cadastrado')
        else:
            dados[nome_do_produto] = {
                "preco" : preco_do_produto,
                "quantidade": quantidade_do_produto
            }
            print(f"Produto {nome_do_produto} cadastrado com sucesso!")

def remover_produto():
    remover = input("Digite o nome do produto para a exclusão: ")
    if remover in dados:
        dados.pop(remover)
    else:
        print("Este produto não existe na base de Dados")

def atualizar_quantidade():
    somar = int(input('Digite [1] para Somar e [2] para Subtrair a quantidade em estoque: '))
    if somar == 1:
        
        produto = input('Digite o produto que deseja adicionar da lista:')
        valor = int(input('Qual valor deseja adicionar no produto: '))
        if produto in dados:
            dados[produto]["quantidade"] += valor
            
def exibir_opcoes():
    print('1. Cadastrar Produtos')
    print('2. Remover produto')
    print('3. Atualizar quantidade')
    print('4. Listar Estoque')
    print('5. Valor total do estoque')
    print('0. Sair')
def main():
    cadastrar_produto()
    remover_produto()

if __name__ == '__main__':
    main()
