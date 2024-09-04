import math

cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

# Tupla con los códigos de las provincias
codigos_provincias = (
    "B", "C", "K", "H", "U", "X", "W", "E", "P", "Y", "L", "F", "M", "N", "Q", "R", "A", "J", "D", "Z", "S", "G", "V",
    "T"
)

# Tupla con los nombres de las provincias
nombres_provincias = (
    "Buenos Aires", "Ciudad Autónoma de Buenos Aires", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes",
    "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquén", "Río Negro", "Salta",
    "San Juan", "San Luis", "Santa Cruz", "Santa Fe", "Santiago del Estero", "Tierra del Fuego", "Tucumán"
)

provincia = "No aplica"
region = None

if len(cp) == 8 and cp[0].isalpha() and cp[1:4].isdigit() and cp[5:7].isalpha():
    pais_del_codigo = "Argentina"
    if cp[0].upper() in codigos_provincias:
        provincia = nombres_provincias[codigos_provincias.index(cp[0].upper())]
    else:
        pais_del_codigo = "Otro"
elif len(cp) == 4 and cp[0:3].isdigit():
    pais_del_codigo = "Bolivia"
elif len(cp) == 9 and cp[0:4].isdigit() and cp[5] == "-" and cp[6:9].isdigit():
    pais_del_codigo = "Brasil"
    if cp[0] in ("0", "1", "2", "3"):
        region = "Brasil0-3"
    elif cp[0] in ("4", "5", "6", "7"):
        region = "Brasil4-7"
    else:
        region = "Brasil8-9"
elif len(cp) == 7 and cp.isdigit():
    pais_del_codigo = "Chile"
elif len(cp) == 6 and cp.isdigit():
    pais_del_codigo = "Paraguay"
elif len(cp) == 5 and cp.isdigit():
    pais_del_codigo = "Uruguay"
    if cp[0] == "1":
        region = "Montevideo"
else:
    pais_del_codigo = "Otro"

precios = 1100, 1800, 2450, 8300, 10900, 14300, 17900
precio = precios[tipo]

if pais_del_codigo in ("Bolivia", "Paraguay") or region in ("Montevideo", "Brasil8-9"):
    precio += precio * 0.20
elif pais_del_codigo in ("Chile", "Uruguay") or region == "Brasil0-3":
    precio += precio * 0.25
elif pais_del_codigo == "Otro":
    precio += precio * 0.50
elif region == "Brasil4-7":
    precio += precio * 0.30

precio_final = precio
if pago == 1:
    precio_final = precio - (precio * 0.10)

print("País de destino del envío:", pais_del_codigo)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", math.trunc(precio))
print("Importe final a pagar:", math.trunc(precio_final))