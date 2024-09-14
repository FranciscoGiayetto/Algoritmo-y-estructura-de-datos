class Publicacion:
    def __init__(self,codigo,titulo,tipo,costo):
        self.codigo=codigo
        self.titulo=titulo
        self.tipo=int(tipo)
        self.costo=int(costo)
    def __str__(self) -> str:
        return f'codigo: {self.codigo} / titulo: {self.titulo} / tipo {self.tipo} / costo {self.costo}'