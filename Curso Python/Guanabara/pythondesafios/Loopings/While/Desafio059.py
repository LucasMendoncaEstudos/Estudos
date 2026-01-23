'''Cire um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso  '''

p_valor = int(input('Digite o primeiro valor: '))
s_valor = int(input('Digite o segundo valor:'))
escolha = 0
while escolha != 5:
    print('''Escolha uma opção do menu:
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa
    ''')
    escolha = int(input('Qual opção você deseja: '))
    if escolha == 1:
        soma = p_valor + s_valor
        print('A soma entre {} e {} é {}.'.format(p_valor, s_valor, soma))
    elif escolha == 2:
        produto = p_valor * s_valor
        print('O resultado de {} x {} é {}'.format(p_valor, s_valor, produto))
    elif escolha == 3:
        if p_valor > s_valor:
            maior = p_valor
        else:
            maior = s_valor
        print('Entre {} e {} o maior valor é {}'.format(p_valor, s_valor, maior))
    elif escolha == 4:
        print('Infortme os números novamente: ')
        p_valor = int(input('Primeiro valor: '))
        s_valor = int(input('Segundo valor:'))
    elif escolha == 5:
        print('Finalizando...')
    else: 
        print('Opção Inválida. Tente Novamente')
    print('=-='* 10)
print('Obrigado')