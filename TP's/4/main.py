from Functions import *


def principal():
    lista_envios = []
    tipo_control = 'Soft Control'
    opcion_int = 0
    acciones = [opcion_1,opcion_2,opcion_3,opcion_4, opcion_5]
    validacion_7 = False 

    while opcion_int != 10:
        mostrar_menu()
        opcion = obtener_opcion()
        if son_numeros(opcion):
            opcion_int = int(opcion)

            if 1 <= opcion_int <= 9:
                if opcion_int == 1:
                    acciones[opcion_int - 1]()
                else:
                    acciones[opcion_int - 1]('envios_pickle.bin')

        else:
            print("\033[1m Opción no válida, ingrese un número.\033[0m")
        


if __name__ == '__main__':
    principal()
