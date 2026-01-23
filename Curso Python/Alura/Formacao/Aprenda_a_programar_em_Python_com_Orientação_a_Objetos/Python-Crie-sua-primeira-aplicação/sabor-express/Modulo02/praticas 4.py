'''
Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.
'''

def cordenadas():
    cord_x = float(input('Digite a cordenada X: '))
    cord_y = float(input('Digite a cordenada Y: '))

    if cord_x > 0 and cord_y > 0 :
        print('Suas cordenadas estão no PRIMEIRO Quadrante do Plano Cartesiano')
    elif cord_x < 0 and cord_y > 0:
        print('Suas cordenadas estão no SEGUNDO Quadrante do Plano Cartesiano')
    elif cord_x < 0 and cord_y < 0:
        print('Suas cordenadas estão no TERCEIRO Quadrante do Plano Cartesiano')
    elif cord_x > 0 and cord_y < 0:
        print('Suas cordenadas estão no QUARTO Quadrante do Plano Cartesiano')
    else:
        print('Suas cordenadas estão na ORIGEM do Plano Cartesiano')


def main():
    cordenadas()
if __name__ == '__main__':
    main()

'''Errei pois não havia colocado as condições para CADA caso, tentei usar atalhos e não funciona :
if cord_x > and cord_y > 0 :
        print('Suas cordenadas estão no PRIMEIRO Quadrante do Plano Cartesiano')'''