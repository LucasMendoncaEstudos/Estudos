'''Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.'''

class Livro:
    def __init__(self, titulo, autor,ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = True

    def __str__(self):
        return f'| {self._titulo} | {self._autor} | {self._ano_publicado} | {self._disponivel}'
    
    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicado == ano and livro._disponivel]
        return livros_disponiveis


livro1 = Livro('Percy jackson', 'Lucas', 2020)
livro2 = Livro('Harryh Potter', 'J K Roling', 2001)
livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f"Antes de emprestar: Livro disponível? {livro3._disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3._disponivel}")

Livro.livros = [livro1, livro2, livro3]