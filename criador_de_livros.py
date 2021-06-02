from livro import Livro

livro1 = Livro(titulo='Teste1', editora='Globo1', autor='Leandro1', ano=2021, isbn=1365491)
livro2 = Livro(titulo='Teste2', editora='Globo2', autor='Leandro2', ano=2022, isbn=1365492)
livro3 = Livro(titulo='Teste3', editora='Globo3', autor='Leandro3', ano=2023, isbn=1365493)

#criar uma lista

livros = [livro1, livro2, livro3]

for livro in livros:
    print(livro)