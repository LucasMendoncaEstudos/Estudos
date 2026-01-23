'''
Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
'''

def login():
    usuario = 'Lucas'
    senha = 1234
    
    dig_usuario = input('Digite o nome de usuário: ')
    dig_senha = int(input('Digite a senha: '))

    if dig_usuario != usuario and dig_senha != senha:
        print('Usuário e senha INCORRETOS')
        
    elif dig_senha != senha:
        print('Senha incorreta')
    elif dig_usuario != usuario:
        print('Nome de usuário Incorreto')
    else:
        print('Pode entrar')


def main():
    login()

if __name__ == '__main__':
    main()

'''Versão alura 
usuario_correto = "alura"
senha_correta = "alura123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")
'''