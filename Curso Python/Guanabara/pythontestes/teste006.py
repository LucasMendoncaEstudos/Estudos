'''nome = str(input('Qual o seu nome? '))
if nome == 'Lucas':
    print('Que nome bonito!')
print('Bom dia, {}'.format(nome))'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua nota foi boa! PARABÉNS!')
else:
    print('Sua nmédia foi ruim! ESTUDE MAIS!')
    
