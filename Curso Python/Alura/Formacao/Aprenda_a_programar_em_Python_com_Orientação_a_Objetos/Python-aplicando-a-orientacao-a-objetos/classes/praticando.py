'''Por exemplo, uma classe Música poderia ter 3 atributos (que trazem as características ou propriedades de um objeto):

nome
artista
duracao
Copiar código
Agora é sua vez! Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos'''


class Musica:
    nome = ''
    artista = ''
    duracao = 0

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista  = 'Jhon Lennon'
musica2.duracao = 183

print(vars(musica1))