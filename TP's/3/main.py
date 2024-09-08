from Functions import *


def principal():
    lista_envios = []
    tipo_control = 'Hard Control'
    opcion_int = 0
    acciones = [opcion_1, opcion_2, opcion_3, opcion_4, opcion_5, opcion_6, opcion_7, opcion_8, opcion_9]
    validacion_7 = False

    while opcion_int != 10:
        mostrar_menu()
        opcion = obtener_opcion()
        if son_numeros(opcion):
            opcion_int = int(opcion)

            if 1 <= opcion_int <= 9:
                if opcion_int == 7:
                    validacion_7 = True

                if opcion_int == 1:
                    tipo_control = acciones[opcion_int - 1](lista_envios, tipo_control)
                elif opcion_int == 8 and not validacion_7:
                    print('\033[1m No se ha seleccionado la opción 7 \033[0m')
                else:
                    acciones[opcion_int - 1](lista_envios, tipo_control)
        else:
            print("\033[1m Opción no válida, ingrese un número.\033[0m")


if __name__ == '__main__':
    principal()