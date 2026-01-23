#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
primeiro_aluno = str(input('Primeiro aluno: '))
segundo_aluno = str(input('Segundo aluno: '))
terceiro_aluno = str(input('Terceiro aluno: '))
quarto_aluno = str(input('Quarto Aluno: '))
lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
escolhido = choice(lista)
print(f'O aluno sorteado foi {escolhido}')