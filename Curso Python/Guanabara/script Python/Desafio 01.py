'''O programa escolhe um número fixo (ex: 7), e o usuário tenta adivinhar. O programa diz se o chute está certo, muito baixo ou muito alto.'''
# Número fixo
fixo = 5

# Entrada do usuário
num = int(input('Tente descobrir o número secreto de 1 a 10: '))

# Verificação
if num < 1 or num > 10:
    print('⚠️ O número precisa estar entre 1 e 10.')
elif num < fixo:
    print('😅 O número está muito baixo, o número secreto é maior.')
elif num == fixo:
    print('🎉 Parabéns! Você achou o número!')
else:
    print('😅 O número está muito alto, o número secreto é menor.')
