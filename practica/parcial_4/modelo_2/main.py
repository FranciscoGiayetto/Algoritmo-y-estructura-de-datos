from funciones import *

def principal():
    opcion=0
    libros=[]
    opciones=[cargar_arreglo,mostrar_arreglo,buscar_isbn,generar_archivo_binario, mostrar_archivo_binario]
    while opcion != 6:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese la opción deseada: "))
            if opcion == 1:
                libros = opciones[opcion - 1](libros)
            elif libros == None:
                print('Primero debe realizar la opcion 1')
            elif 2 <= opcion <= 5:
                opciones[opcion - 1](libros)
            else:
                print('Opcion no valida')
        except ValueError:
            print('La opcion ingresada no es un numero')

if __name__ == '__main__':
    principal()
