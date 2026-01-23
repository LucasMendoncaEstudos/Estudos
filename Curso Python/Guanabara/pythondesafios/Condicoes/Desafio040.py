'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
-média abaixo de 5.0:
REPROVADO
-Média entre 5.0 e 6.9:
RECUPERAÇÃO
-Média 7.0 ou superior:
APROVADO'''
print('Vamos saber sua situação na média')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2

print('Tirando {:.1f} e {:.1f}, a média do aluino é de {:.1f}'.format(n1, n2, media))

if media < 5.0:
    print('RREPOVADO!')
elif media <= 5 and media <= 6.9:
    print("RECUPERAÇÃO")
else:
    print('APROVADO!!')