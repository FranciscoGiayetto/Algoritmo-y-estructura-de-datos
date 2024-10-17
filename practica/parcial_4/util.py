def ordenamiento(lista, objeto):
    longitud = len(lista)
    posicion = longitud
    izquierda = 0
    derecha = longitud - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio].nombre == objeto.nombre:
            posicion = medio
            break
        if objeto.nombre < lista[medio].nombre:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    if izquierda > derecha:
        posicion = izquierda
    lista[posicion:posicion] = [objeto]

import random
def cargar_datos():
    nombres = ['aOrge', 'bepe', 'cuan', 'dedro', 'eeon']
    nombre = random.choice(nombres)
    numero_manzana = random.randint(1, 35)

def matriz_contadores(lista):
    longitud = len(lista)
    #primeras columnas - segunda filas
    matriz = [[0] * 4 for _ in range(35)]
    for i in range(longitud):
        fila = lista[i].numero_manzana - 1
        columna = lista[i].orientacion - 1
        matriz[fila][columna] += lista[i].superfie

    for fila in range(35):
        for columna in range(4):
            if matriz[fila][columna] != 0:
                print("Manzana:", fila + 1, "Orientación:", columna + 1, "Superficie:", matriz[fila][columna])
    print()

    m = int(input("Manzana que desea acumular (entre 1 y 35)?: "))
    sa = 0
    fila = m - 1
    for columna in range(4):
        sa += matriz[fila][columna]
    print("La superficie total para la manzana", m, "es:", sa)
    print()

import pickle
import os
def archivo_bianrio(i):
    # Verifica si el archivo 'datos.bin' existe en el sistema
    if not os.path.exists('datos.bin'):
        print("No existe el archivo", 'datos.bin', "...")
        return  # Si el archivo no existe, sale de la función

    # Abre el archivo binario 'datos.bin' en modo de escritura binaria ('wb' sobrescribe el archivo)
    archivo_binario = open('datos.bin', 'wb')

    # Obtiene el tamaño del archivo (esto no tiene sentido aquí ya que 'os.path.getsize()' requiere un archivo)
    # Además, falta el argumento para el nombre del archivo. Esto probablemente dará error.
    tamaño_archivo = os.path.getsize()

    # Guarda la posición actual en el archivo binario (aunque esto no es necesario al inicio)
    pepe = archivo_binario.tell()

    # Intenta cargar un objeto del archivo binario (esto es incorrecto en este contexto, ya que el archivo se abrió para escribir)
    lote = pickle.load(archivo_binario)  # Esto fallará porque se abrió en modo 'wb', debería ser 'rb' para leer

    # Guarda el objeto 'i' en el archivo binario
    pickle.dump(i, archivo_binario)
    
    # Cierra el archivo después de escribir el objeto
    archivo_binario.close()

def busqueda_binaria(lista, objetivo):
    """
    Realiza una búsqueda binaria en una lista ordenada.
    
    Args:
        lista (list): Una lista de elementos ordenados.
        objetivo (any): El elemento que se desea buscar en la lista.
        
    Returns:
        int: La posición del elemento objetivo en la lista, o -1 si no se encuentra.
    """
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # Calcula el índice del medio
        valor_medio = lista[medio]  # Obtiene el valor en el índice medio

        # Verifica si el valor medio es igual al objetivo
        if valor_medio == objetivo:
            return medio  # Retorna la posición del elemento encontrado

        # Si el valor medio es menor que el objetivo, busca en la mitad derecha
        elif valor_medio < objetivo:
            izquierda = medio + 1  # Ajusta el límite izquierdo

        # Si el valor medio es mayor que el objetivo, busca en la mitad izquierda
        else:
            derecha = medio - 1  # Ajusta el límite derecho

    return -1  # Retorna -1 si el elemento no se encuentra