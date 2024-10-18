def mostrar_menu():
    print('MENU')

def es_negativo(valor):
    return valor < 0 
import random
from clase import Pantalon

def agregar_en_orden(lista,objeto):
    longitud=len(lista)
    posicion= longitud
    derecha= longitud-1
    izquierda=0
    while izquierda <= derecha:
        medio= (derecha+izquierda)// 2
        if lista[medio].codigo == objeto.codigo:
            posicion= medio
        
        if lista[medio].codigo > objeto.codigo:
            derecha= medio - 1
        else:
            izquierda= medio + 1
    if izquierda > derecha:
        posicion= izquierda
    lista[posicion:posicion]=[objeto]

def cargar_datos_arreglo(lista):
    negativo=True
    while negativo:
        cantidad_datos=int(input('Ingrese la cantidad de datos a cargar: '))
        if es_negativo(cantidad_datos):
            print('La cantidad de datos no puede ser negativa')
        else:
            negativo=False
    nombres=['pepe','juan','otro']
    for i in range(cantidad_datos):
        codigo= random.randint(0,100)
        nombre=random.choice(nombres)
        talle_largo= random.randint(30,50)
        talle_cintura= random.randint(30,50)
        tipo_tela= random.randint(1,3)
        stock= random.randint(0,100)

        pantalon=Pantalon(codigo,nombre,talle_largo,talle_cintura,tipo_tela,stock)
        agregar_en_orden(lista,pantalon)
    return lista

def mostrar_elementos(lista):
    for i in lista:
        print(i.__str__())

def calcular_stock_disponible(lista):
    valor= int(input('Ingrese el valor para filtrar: '))
    #columnas= talle de largo fila=talle de cintura
    matriz=[[0]*21 for i in range(21)]
    for i in lista:
        fila= i.talle_largo -30
        columna= i.talle_cintura - 30
        matriz[fila][columna] += i.stock
    
    for fila in range(21):
        for columna in range(21):
            if matriz[fila][columna] > valor:
                print(f'Talle de largo: {fila + 30} - Talle de cintura {columna + 30} - cantidad {matriz[fila][columna] }')

import pickle
def generar_archivo_binario(lista):
    tipo_tela_agregar= int(input('Ingresa el numero del tipo de tela que quiere agregar: '))
    if 1 <= tipo_tela_agregar <=3:
        archivo_binario=open('pantalones.bin','wb')
        for i in lista:
            if i.tipo_tela == tipo_tela_agregar and i.stock > 0:
                pickle.dump(i,archivo_binario)
        archivo_binario.close()
    else:
        print('Ese tipo no existe')

import os
def mostrar_archivo_binario(lista):
    if not os.path.exists('pantalones.bin'):
        return print('El archivo binario no existe!')
    
    archivo_binario=open('pantalones.bin','rb')
    largo_archivo= os.path.getsize('pantalones.bin')
    cantidad_datos=0
    suma_datos=0
    while archivo_binario.tell() < largo_archivo:
        pantalon= pickle.load(archivo_binario)
        print(pantalon)
        cantidad_datos += 1
        suma_datos += pantalon.stock
    
    print(f'El promedio es {suma_datos/ cantidad_datos}')
