class Envio:
    def __init__(self, codigo, direccion, tipo, forma_pago, pais):
        self.codigo = codigo
        self.direccion = direccion
        self.tipo = tipo
        self.forma_pago = forma_pago
        self.pais = pais

    def mostrar(self):
        return (
        f"[Código: {self.codigo}]  "
        f"[Dirección: {self.direccion}]  "
        f"[Tipo de Envío: {self.tipo}]  "
        f"[Forma de Pago: {self.forma_pago}]  "
        f"[País: {self.pais}]"
    )