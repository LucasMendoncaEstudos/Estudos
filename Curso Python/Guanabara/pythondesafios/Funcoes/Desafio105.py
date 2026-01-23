""" Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retronar um dicionário com as seguintes informações: 
-Quantidade de notas
-A maior nota
-A menor nota
-A média da turma
-A situação(opicional)

Adicione também as docstrings da função
"""

def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    n: uma ou mais notas dos alunos (aceita várias)
    sit: valor opicional, indicando se deve ou não adicionar a situação
    return: dicionário com várias informações sobre a situação da turma
    """
    dicio = dict()
    dicio['total'] = len(nota)
    dicio['maximo'] = max(nota)
    dicio['minimo'] = min(nota)
    dicio['media'] = sum(nota)/len(nota)
    
    if sit:
        if dicio['media'] >= 7:
            dicio['situação'] = 'Boa'
        elif dicio['media'] >= 5:
            dicio['situação'] = 'Razoável' 
        else:
            dicio['situação'] = 'Ruim'
    return dicio

resp = (notas(4.5, 9.9, 10, sit=True))
print(resp)