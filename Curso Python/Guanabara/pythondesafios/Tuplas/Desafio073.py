'''Crie uma tupla preenchida com os 20 primeiros colocados ta Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.Depois mostre:
A)Apenas os 5 primeiros colocados.
B)Os últimos 4 colocados da tabela.
C)Uma lista com os time em ordem alfabética.
D)Em que posição na tabela está o time do Flamengo.'''

times = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Internacional', 'Atlético-PR','Atlético-MG', 'Santos', 'América-MG', 'Bragantino', 'Goiás', 'São Paulo', 'Fortaleza', 'Botafogo', 'Ceará SC', 'Cuiabá', 'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')


print(f'Os 5 primeiros são : {times[:5]}')

print(f'Os 4 Ultimos colcados são {times[-4:]}')

print(f'A lista de times em ordem alfabética é {sorted(times)}')

print(f'O time do flamengo esta na posição {times.index('Flamengo') + 1}')