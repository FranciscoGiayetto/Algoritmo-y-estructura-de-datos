class Ticket():
    def __init__(self,codigo_vuelo,numero_pasajero,pais_destino,numero_asiento, importe):
        self.codigo_vuelo= codigo_vuelo
        self.numero_pasajero=numero_pasajero 
        self.pais_destino=pais_destino
        self.numero_asiento=numero_asiento
        self.importe=importe
    def __str__(self) :
        return (f'codigo vuelo: {self.codigo_vuelo} / numero pasajero: {self.numero_pasajero} / numero de asiento: {self.numero_asiento} ')