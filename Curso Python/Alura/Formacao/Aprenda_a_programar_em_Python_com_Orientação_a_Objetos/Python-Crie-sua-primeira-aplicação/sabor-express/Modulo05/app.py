'''Praticando Docstrings
Crie uma docstring para a função exibir_nome_do_programa()
Crie uma docstring para a função exibir_opcoes()
Crie uma docstring para a função finalizar_app()
Crie uma docstring para a função opcao_invalida()
Crie uma docstring para a função exibir_subtitulo(texto)
Crie uma docstring para a função cadastrar_novo_restaurante()
Crie uma docstring para a função listar_restaurantes()
Crie uma docstring para a função alternar_estado_restaurante()
Crie uma docstring para a função escolher_opcao()
Crie uma docstring para a função main()
'''

import os

restaurantes = [{'nome':'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome':'Pizza Suprema', 'categoria': 'Italiana', 'ativo': True},
                {'nome':'Cantina', 'categoria': 'Teste', 'ativo': False}
                ]
def exibir_nome_do_programa():
    '''
    Função para exibir o nome do programa já formatado
    '''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''
    Função para exibir as opções onde o usuário irá selecionar
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''
    Função para quando finalizar o aplicativo, informar para o usuário
    '''
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    '''
    Função para retornar para o menu principal

    Input:
    Digitar qualquer tecla para retornar ao menu

    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def exibir_subtitulo(texto):
    '''
    Exibe um subtítulo estilizado na tela 
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    ''' 
    Exibe mensagem de opção inválida e retorna ao menu principal 
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    -Categoria
    
    Output:
    Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    '''
    Altera o estado ativo/desativado de um restaurante 
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()


def listar_rastaurantes():
    '''
    Lista os restaurantes presentes na lista 
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Lista de Restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | Status ')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def escolher_opcao():
    ''' 
    Solicita e executa a opção escolhida pelo usuário 
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_rastaurantes()
        elif opcao_escolhida == 3: 
            alterar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''

    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()