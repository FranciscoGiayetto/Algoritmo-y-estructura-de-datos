class Envio:
    def __init__(self,codigo,direccion,tipo,forma_pago, hard_control, importe=0):
        self.codigo= codigo
        self.direccion= direccion
        self.tipo= tipo
        self.forma_pago= forma_pago
        self.importe = importe 
        self.hard_control = hard_control

    def __str__(self):
        return str(self.codigo)
    
    def mostrar(self):
        return f"Codigo: {self.codigo} Dirección: {self.direccion} Tipo de envio {self.tipo} Forma de Pago {self.forma_pago}"