class Envio:
    def __init__(self, codigo, direccion, tipo, forma_pago, valido, hard_control='Hard Control', importe=0, pais=None):
        self.codigo= codigo
        self.direccion= direccion
        self.tipo= tipo
        self.forma_pago= forma_pago
        self.importe = importe 
        self.hard_control = hard_control
        self.pais = pais
        self.valido = valido

    def __str__(self):
        return str(self.codigo)
    
    def mostrar(self):
        return f"Codigo: {self.codigo} / Dirección: {self.direccion} / Pais: {self.pais} / Importe: {self.importe} / Tipo de envio {self.tipo} / Forma de Pago {self.forma_pago} / Control: {self.hard_control} / Valido: {self.valido}"