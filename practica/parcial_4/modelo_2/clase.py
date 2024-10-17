class Libro:
    def __init__(self, isbn,titulo,autor,codigo_idioma,precio):
        self.isbn= isbn
        self.titulo=titulo
        self.autor=autor
        self.codigo_idioma=codigo_idioma
        self.precio=precio
        
    def __str__(self):
        idiomas=['Español','Ingles','Portugues','Frances','Italiano']
        return f'isbn: {self.isbn} titulo: {self.titulo} autor: {self.autor} idioma: {idiomas[int(self.codigo_idioma) - 1]} precio: {self.precio} '