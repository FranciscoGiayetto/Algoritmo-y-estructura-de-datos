import random
from clase import Pieza
import pickle
import os

def mostrar_menu():
    print('============ MENU =============================')
    print('1- Cargar arreglo de con datos de piezas')
    print('2- Mostrar las piezas con stock reducido')
    print('3-Determinar el valor acumulado en stock por tipo de pieza')
    print('4- Generar archivo binario')
    print('5- Mostrar archivo binario')
    print('6- Salir')
    print('===============================================')
    print()

def es_negativo(valor):
    return valor < 0


def generar_datos():
    descripciones=['1','2','3']
    codigo_identificacion= random.randint(0, 100000)
    descripcion=random.choice(descripciones)
    tipo_pieza=random.randint(0,19)
    numero_sector=random.randint(10,25)
    stock= random.randint(0, 100000)

    return Pieza(codigo_identificacion,descripcion,tipo_pieza,numero_sector,stock)


def agregar_ordenado_en_lista(objeto,lista):
    longitud=len(lista)
    posicion= longitud
    derecha= longitud-1
    izquierda= 0

    while izquierda <= derecha:
        medio= (derecha+ izquierda) // 2
        if lista[medio].codigo_identificacion == objeto.codigo_identificacion:
            posicion= medio
        
        if lista[medio].codigo_identificacion > objeto.codigo_identificacion:
            derecha= medio - 1
        else:
            izquierda= medio +1
    if izquierda > derecha:
        posicion= izquierda
    lista[posicion:posicion]=[objeto]

def generar_arreglo_ordenado(lista):
    fin= True
    while fin:
        cantidad_datos= int(input('Ingrese la cantidad de datos a generar: '))
        if es_negativo(cantidad_datos):
            print('La cantidad de datos no puede ser negativa')
        else:
            fin= False
    for i in range(cantidad_datos):
        pieza=generar_datos()
        agregar_ordenado_en_lista(pieza,lista)

def mostrar_arreglo(lista):
    stock_minimo= int(input('Ingrese la cantidad de stock minimo: '))
    for i in lista:
        if i.stock < stock_minimo:
            print(i.__str__(), ' Stock reducido ')
        else:
            print(i.__str__())

def determinar_valor_acumulado_stock(lista):
    matriz=[[0]*20 for j in range(16)]
    for i in lista:
        fila= i.numero_sector - 10
        columna= i.tipo_pieza
        matriz[fila][columna]+= i.stock
    
    for fila in range(16):
        for columna in range(20):
            if matriz[fila][columna] > 0:
               print(f'Tipo: {columna} Sector: {fila + 10 } Cantidad: {matriz[fila][columna]}')



def generar_archivo_binario(lista):
    archivo_binario= open('piezas.bin','wb')
    for i in lista:
        if i.numero_sector > 15:
            pickle.dump(i,archivo_binario)
    archivo_binario.close()

def mostrar_archivo_binario(lista):
    if not os.path.exists('piezas.bin'):
        print('El archivo binario aun no fue creado')
        return
    
    archivo_binario= open('piezas.bin','rb')
    longitud= os.path.getsize('piezas.bin')
    suma_stock=0
    cantidad_piezas=0
    if longitud != 0:
        while archivo_binario.tell() < longitud:
            pieza= pickle.load(archivo_binario)
            print(pieza)
            suma_stock += pieza.stock
            cantidad_piezas += 1
        
        print(f'El promedio fue {suma_stock/cantidad_piezas}')
    else:
        print(f'El archivo binario esta vacio.')