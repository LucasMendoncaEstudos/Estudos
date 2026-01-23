'''
Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado
Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.

Saída esperada:
Digite a primeira nota:4
Digite a Segunda nota 6.3:
Digite a terceira nota 8.9:
media: 6.77
Recuperação
'''

def situacao_escolar():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a primeira nota: '))
    nota3 = float(input('Digite a primeira nota: '))
    media = (nota1 + nota2 + nota3) / 3
    print(f'Sua média é de {media:.2f}')
    if media < 5:
        print('Você esta reprovado!')
    elif 5 <= media < 7:
        print('Você esta de Recuperação')
    else:
        print('Você foi Aprovado')
    
def main():
    situacao_escolar()

if __name__=='__main__':
    main()