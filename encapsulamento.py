class Livro:

    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.autor = autor

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo



livro1 = Livro('Curso de Python', 'Leandro Serra')
print(livro1.autor)
print(livro1.titulo)
livro1.titulo = 'Novo livro'
print(livro1.titulo)