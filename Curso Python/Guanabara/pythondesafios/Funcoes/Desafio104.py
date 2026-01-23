"""Crie um programa que tenha a função leiaInt(), que vai funcioar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Exemplo de uso:
python
n = leiaInt("Digite um número: ")"""

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número ínteiro válido. \033[m')
        if ok == True:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')