

participantes = list()
dados = list()
for p in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    participantes.append(dados[:])
    dados.clear()

print(f'Lista de participantes: {participantes}')

for p in participantes:
    if p[1] >= 100:
        print(f'O participante {p[0]} não pode competir, pois esta acima do peso')
