import random
from clase import Lote
import pickle

def ordenamiento(lista, objeto):
    n = len(lista)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if lista[c].nombre == objeto.nombre:
            pos = c
            break
        if objeto.nombre < lista[c].nombre:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    lista[pos:pos] = [objeto]


def cargar_datos():
    nombres = ['aOrge', 'bepe', 'cuan', 'dedro', 'eeon']
    apellidos = ['gomez', 'juarez', 'eso']
    
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    numero_manzana = random.randint(1, 35)
    numero_lote = random.randint(1, 20)
    orientacion = random.randint(1, 4)
    superficie = random.randint(1, 1000)
    monto = random.randint(50, 5000)

    lote = Lote(superficie, nombre, apellido, numero_manzana, numero_lote, orientacion, monto)
    return lote


def opcion_1():
    while True:
        n = int(input('Ingrese los datos a cargar: '))
        if not n > 0:
            print('Ingrese un número positivo')
        else:
            break
    lista = []
    for i in range(n):
        ordenamiento(lista, cargar_datos())
    return lista


def opcion_2(lista):
    print(lista)
    for i in lista:
        print(i.mostrar())


def opcion_3(lista):
    n = len(lista)

    ac = [[0] * 4 for _ in range(35)]
    for i in range(n):
        f = lista[i].numero_manzana - 1
        c = lista[i].orientacion - 1
        ac[f][c] += lista[i].superfie

    for f in range(35):
        for c in range(4):
            if ac[f][c] != 0:
                print("Manzana:", f + 1, "Orientación:", c + 1, "Superficie:", ac[f][c])
    print()

    m = int(input("Manzana que desea acumular (entre 1 y 35)?: "))
    sa = 0
    f = m - 1
    for c in range(4):
        sa += ac[f][c]
    print("La superficie total para la manzana", m, "es:", sa)
    print()

def opcion_4(lista):
    l1=int(input('Ingrese el numero de lote para filtrar(menor): '))
    l2=int(input('Ingrese el numero de lote para filtrar(mayor): '))

    archivo_binario = open('datos.bin', 'wb')

    for i in lista:
        if l1 <= i.numero_lote <= l2:
            pickle.dump(i, archivo_binario)
    
    archivo_binario.close()
import os
def opcion_5(lista):
    if not os.path.exists('datos.bin'):
        print("No existe el archivo", 'datos.bin', "...")
        return
    fd='datos.bin'
    print("Listado de lotes...")

    cantidad_lotes = 0
    total_importe = 0

    # Abrir el archivo en modo lectura binaria
    archivo_binario = open(fd, "rb")

    # Obtener el tamaño total del archivo
    tamaño_archivo = os.path.getsize(fd)

    # Leer el archivo mientras no hayamos alcanzado el final
    while archivo_binario.tell() < tamaño_archivo:
        lote = pickle.load(archivo_binario)  # Cargar el objeto Lote desde el archivo
        cantidad_lotes += 1
        total_importe += lote.monto  # Suponiendo que "importe" es "monto" en el objeto Lote
        print(lote)  # Mostrar cada lote

    # Cerrar el archivo después de la lectura
    archivo_binario.close()

    # Calcular y mostrar el promedio si hay lotes
    if cantidad_lotes > 0:
        promedio = total_importe / cantidad_lotes
        print(f"El valor promedio de venta de los lotes es: {promedio:.2f}")
    else:
        print("No se encontraron lotes en el archivo.")

def principal():
    opciones = [opcion_1, opcion_2, opcion_3, opcion_4,opcion_5]
    opcion = 1
    lotes = []
    while  1 <= opcion <= 5:
        opcion = int(input('Ingrese la opción: '))
        if opcion == 1:
            lotes = opciones[opcion - 1]()
        elif 2 <= opcion <= 5:
            if lotes:
                opciones[opcion - 1](lotes)
            else:
                print('Vector no creado')


if __name__ == '__main__':
    principal()
