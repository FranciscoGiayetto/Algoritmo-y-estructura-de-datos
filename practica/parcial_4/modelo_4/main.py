from functions import *

def principal():
    piezas=[]
    opcion=0
    opciones=[generar_arreglo_ordenado, mostrar_arreglo,determinar_valor_acumulado_stock,generar_archivo_binario, mostrar_archivo_binario]
    while opcion != 6:
        try:
            mostrar_menu()
            opcion=int(input('Ingrese la opcion que desea utilizar: '))
            if opcion == 1:
                opciones[opcion -1](piezas)
            
            if 2 <= opcion <= 6:
                if opcion == 5:
                    opciones[opcion -1](piezas)
                elif piezas == []:
                    print('Vector no generado ingrese la opcion 1')
                else:
                    opciones[opcion -1](piezas)
            else:
                print('Opcion no permitida')
        except ValueError:
            print('Error: ingrese un numero como opcion.')
            

if __name__ == '__main__':
    principal()