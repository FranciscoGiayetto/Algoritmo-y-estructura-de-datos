class Lote(): 
    def __init__(self, superfie, nombre, apellido, numero_manzana, numero_lote, orientacion, monto):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_manzana = numero_manzana
        self.numero_lote = numero_lote
        self.orientacion = orientacion
        self.superfie = superfie
        self.monto = monto

    def mostrar(self):
        orientacion=['Norte','Sur','Este','Oeste']
        return f'nombre: {self.nombre} - orientacion: {orientacion[self.orientacion -1]} '