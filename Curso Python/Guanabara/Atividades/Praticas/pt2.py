'''lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

for cont in range(0,len(lanche)):
    print(lanche[cont])'''
'''
Permita o usuário inserir nomes em uma lista

Mostre a quantidade total de nomes cadastrados

Exiba os nomes em ordem alfabética

Permita verificar se um nome já foi cadastrado'''

nomes = []


while True:
    print('Menu')
    print('[1] Cadastrar novo nome\n [2]Ver todos os Nomes\n [3] Procurar um nome\n [4] Sair')
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        while True:
            nome = str(input('Digite um nome :'))
            nomes.append(nome)
            outro = str(input('Quer adicionar outro nome ? [S/N]: ').strip().upper()[0])
            if outro == 'N':
                break
    if opcao == 2:
        print(f'Aqui estão todos os nomes: {nomes}')
    if opcao ==3:
        i = print(input('Qual nome voce quer Procurar ?: '))
        if i in nomes:
            print(f'O nome {i} esta sim na lista')
        else: 
            print('Desculpe o nome não esta na lista')
    if opcao == 4:
        break

        
    