'''
Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

Saída esperada:
Digite a temperatura atual: 30
Alerta! Temperatura acima do limite permitido.
'''

def temperatura():
    graus = float(input('Digite a temperatura atual em Graus Celcius da sala de servidores: '))
    if graus > 25:
        print('ALERTA ! Temperatura acima do limite permitido.')
    else:
        print('Temperatura dentro do limite seguro!')

def main():
    temperatura()

if __name__=='__main__':
    main()