'''Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

'''
def idade(ano_nascimento, ano_atual):
    calculo = ano_atual - ano_nascimento
    return calculo

def main():
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    ano_atual = int(input('Digite o ano atual: '))
    idades = idade(ano_nascimento, ano_atual)
    print(f'A idade é {idades} anos')
if __name__ == '__main__':
    main()