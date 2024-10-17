def mostrar_menu():
    print('======== MENU ==========')
    print('1- Cargar datos de libros ')
    print('2- Mostrar libros ')
    print('3- Buscar por isbn ')
    print('4- Generar archivo binario ')
    print('5- Mostrar archivo generado ')
    print('6- Salir ')
    print('========================')

def busqueda_binaria(objetivo,lista):
    objetivo=int(objetivo)
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # Calcula el índice del medio
        valor_medio = lista[medio].isbn  # Obtiene el valor en el índice medio

        # Verifica si el valor medio es igual al objetivo
        if valor_medio == objetivo:
            return medio  # Retorna la posición del elemento encontrado

        # Si el valor medio es menor que el objetivo, busca en la mitad derecha
        elif valor_medio < objetivo:
            izquierda = medio + 1  # Ajusta el límite izquierdo

        # Si el valor medio es mayor que el objetivo, busca en la mitad izquierda
        else:
            derecha = medio - 1  # Ajusta el límite derecho

    return None

def agregar_ordenado_isbn(objeto,lista):
    longitud=len(lista)
    posicion= longitud
    derecha= longitud - 1
    izquierda= 0
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if objeto.isbn == lista[medio].isbn:
            posicion=medio
            break

        if objeto.isbn > lista[medio].isbn:
            izquierda=medio + 1
        else:
            derecha=medio -1
        
    if izquierda > derecha:
        posicion= izquierda
        
    lista[posicion:posicion]=[objeto]
    return lista

import random
from clase import Libro

def cargar_arreglo(lista):
    cantidad_datos= int(input('Ingrese la cantidad de datos a cargar: '))
    titulos=['Peter Pan','Pepe el curioso', 'Tiutlo 2']
    autores=['Homero','Messi','Da Vinci']
    if cantidad_datos > 0:
        for i in range(cantidad_datos):
            isbn= random.randint(1000000000000,9999999999999)
            titulo=random.choice(titulos)
            autor= random.choice(autores)
            codigo_idioma=random.randint(1,5)
            precio=random.randint(0,1000000)

            libro=Libro(isbn,titulo,autor,codigo_idioma,precio)

            agregar_ordenado_isbn(libro,lista)
        
    else:
        print('Ingrese un numero positivo')
    return lista

def mostrar_arreglo(lista):
    for i in lista:
        print(i.__str__())

def buscar_isbn(lista):
    isbn= input('Ingrese el isbn del libro a buscar: ')
    posicion=busqueda_binaria(isbn,lista)
    if posicion == None:
        print(f'No contamos con el libro {isbn} pero no deje de visitar nuestra sección de ofertas!')
    else:
        print(lista[posicion])
        if lista[posicion].codigo_idioma == 4:
            print('Es frances descuento')
            lista[posicion].precio= int(lista[posicion].precio) - ((int(lista[posicion].precio) * 22)/ 100)
            print(lista[posicion])

import pickle
def generar_archivo_binario(lista):
    autor=input('Ingrese el autor: ')
    precio=int(input('Ingrese el precio que no tiene q superar: '))
    archivo_binario= open('libros.bin','wb')
    for i in lista:
        if i.autor == autor and i.precio <= precio:
            pickle.dump(i,archivo_binario)
    archivo_binario.close()

import os
def mostrar_archivo_binario(lista):
    if not os.path.exists('libros.bin'):
        return print('El archivo binario aun no existe')
    
    archivo_binario= open('libros.bin','rb')
    tamaño_archivo = os.path.getsize('libros.bin')
    contador=0

    while archivo_binario.tell() < tamaño_archivo:
        datos= pickle.load(archivo_binario)
        print(datos)
        contador +=1

    print('Cantidad de datos: ', contador)
    archivo_binario.close()