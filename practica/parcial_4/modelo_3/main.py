
from funtions import *
def principal():
    opciones=[cargar_datos_arreglo,mostrar_elementos, calcular_stock_disponible,generar_archivo_binario, mostrar_archivo_binario]
    pantalones=[]
    opcion=0
    while opcion != 6:
        mostrar_menu()
        opcion= int(input('Ingrese su opcion: '))
        if opcion == 1:
            pantalones = opciones[opcion - 1](pantalones)
        elif 2 <= opcion <= 5:
            if pantalones:
                opciones[opcion - 1](pantalones)
            else:
                print('No se ha creado el arreglo. Primero cargue los datos.')
        elif opcion == 6:
            print('Saliendo del programa...')
        else:
            print('Opción no permitida')


if __name__ == '__main__':
    principal()