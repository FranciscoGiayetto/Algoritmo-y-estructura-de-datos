class Pieza:
    def __init__(self,codigo_identificacion,descripcion,tipo_pieza,numero_sector,stock):
        self.codigo_identificacion= codigo_identificacion
        self.descripcion= descripcion
        self.tipo_pieza= tipo_pieza
        self.numero_sector= numero_sector
        self.stock= stock
    def __str__(self):
        return f'codigo de identificacion: {self.codigo_identificacion} - descripcion: {self.descripcion} - tipo de pieza: {self.tipo_pieza} - numero de sector: {self.numero_sector} - stock: {self.stock}'
    