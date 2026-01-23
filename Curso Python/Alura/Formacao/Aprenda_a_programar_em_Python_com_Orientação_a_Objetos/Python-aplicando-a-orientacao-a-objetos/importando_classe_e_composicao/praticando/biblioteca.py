from pratica import Livro

livro_biblioteca = Livro("python in practice", 'Emily Coder', 2021)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca._disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca._disponivel}")

ano = 2020

livros_disponiveis = Livro.verificar_disponibilidade(ano)
print(f'Livros disponiveis em {ano}: {livros_disponiveis}')