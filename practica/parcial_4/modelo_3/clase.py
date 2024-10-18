class Pantalon:
    def __init__(self,codigo,nombre,talle_largo,talle_cintura,tipo_tela,stock):
        self.codigo= codigo
        self.nombre= nombre
        self.talle_largo= talle_largo
        self.talle_cintura= talle_cintura
        self.tipo_tela= tipo_tela
        self.stock= stock

    def __str__(self):
        descripciones=['Jean','Gabardina','Denim']
        return (f"Código: {self.codigo}, Nombre: {self.nombre}, Talle largo: {self.talle_largo}, "
                f"Talle cintura: {self.talle_cintura}, Tipo de tela: {descripciones[int(self.tipo_tela)-1]}, Stock: {self.stock}")
