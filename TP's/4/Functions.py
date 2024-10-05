import os
import pickle

def son_numeros(cadena):
    for letra in cadena:
        if letra not in ('0123456789'):
            return False
    return True

def mostrar_menu():
    print("\n" + "=" * 40)
    print(" " * 10 + "MENU PRINCIPAL")
    print("=" * 40)
    print("1 - Cargar datos desde archivo binario")
    print("2 - Ingresar datos manualmente")
    print("3 - Mostrar todos los envíos")
    print("4 - Buscar envío por Código Postal")
    print("5 - Buscar envío por Dirección")
    print("6 - Salir")
    print("=" * 40 + "\n")


def obtener_opcion():
    return input("Por favor, elige una opción: ")


def confirmar_eliminar_archivo():
    confirmacion = input("Advertencia: el archivo binario existente será eliminado. ¿Desea continuar? (s/n): ")
    return confirmacion.lower() == 's'

def crear_archivo_binario(archivo_csv, archivo_binario):
    if not os.path.exists(archivo_csv):
        print(f"Error: El archivo '{archivo_csv}' no existe.")
        return

    if not confirmar_eliminar_archivo():
        print("Operación cancelada.")
        return

    if os.path.exists(archivo_binario):
        os.remove(archivo_binario)

    with open(archivo_csv, 'r') as file_csv:
        file_csv.readline() 
        file_csv.readline()  
        with open(archivo_binario, 'wb') as file_binario:
            for linea in file_csv:
                row = linea.strip().split(',')
                envio = Envio(
                    codigo=row[0],       
                    direccion=row[1],    
                    tipo=row[2],        
                    forma_pago=row[3],
                    pais= calcular_pais(row[0]) 
                )
                pickle.dump(envio, file_binario)

    print(f"Archivo binario '{archivo_binario}' creado con éxito.")


def mostrar_contenido_binario(archivo_binario):
    print("\nContenido del archivo binario:")
    i=0
    with open(archivo_binario, 'rb') as binfile:
        try:
            while True:
                envio = pickle.load(binfile)
                print(envio.mostrar())
        except:
            pass  



def opcion_1():
    archivo_csv = 'envios-tp4.csv'
    archivo_binario = 'envios_pickle.bin'

    crear_archivo_binario(archivo_csv, archivo_binario)
    return archivo_binario

def opcion_2(archivo_binario):
    carga_teclado(archivo_binario)

def opcion_3(archivo_binario):
    mostrar_contenido_binario(archivo_binario)

def opcion_4(archivo_binario):
    codigo_buscar=input('Ingrese el codigo postal a buscar: ')
    busqueda_codigo_postal(archivo_binario,codigo_buscar)

def opcion_5(archivo_binario):
    direccion=input('Ingrese la direccion a buscar: ')
    busqueda_direccion(archivo_binario,direccion)



#2

from clase import Envio
def normalizacion_codigo_postal(codigo_postal):
    codigo_postal_sin_espacios = ''
    for i in codigo_postal:
        if i != ' ':
            codigo_postal_sin_espacios += i
    return codigo_postal_sin_espacios


def normalizacion_direccion(direccion):
    direccion_sin_espacios = ''
    for i in range(1, len(direccion)):
        if direccion[-i] not in ' .':
            if i != 1:
                direccion_sin_espacios = direccion[:-i + 1]
            else:
                direccion_sin_espacios = direccion
            break
    return direccion_sin_espacios


def verificacion_envio(tipo_envio):
    if tipo_envio in (0, 1, 2):
        return 'Carta simple'
    elif tipo_envio in (3, 4):
        return 'Carta certificada'
    else:
        return 'Carta express'


def validacion_tipo_envio(tipo_envio):
    if tipo_envio in (0, 1, 2, 3, 4, 5, 6):
        return True
    else:
        return False

def veiificacion_forma_pago(valor):
    return valor in [1, 2]


def carga_teclado(archivo_binario):
    codigo_postal = normalizacion_codigo_postal(input('Ingrese el código postal: '))
    direccion = normalizacion_direccion(input('Ingrese la dirección: '))
    continuar = True

    while continuar:
        tipo_envio = int(input(
            '------------------\n'
            '0 - Carta Simple\n'
            '1 - Carta Simple\n'
            '2 - Carta Simple\n'
            '3 - Carta Certificada\n'
            '4 - Carta Certificada\n'
            '5 - Carta Expresa\n'
            '6 - Carta Expresa\n'
            '------------------\n'
            'Ingrese el tipo de envío (0-6):'
        ))
        if validacion_tipo_envio(tipo_envio):
            continuar = False
        else:
            print('\033[1m El tipo de envío no es válido\033[0m')
    continuar = True
    while continuar:
        forma_pago = int(input('Ingrese la forma de pago (1-efectivo, 2-tarjeta de crédito): '))
        if veiificacion_forma_pago(forma_pago):
            continuar = False
        else:
            print('\033[1m La forma de pago no es válida\033[0m')
    
    envio = Envio(codigo_postal, direccion, tipo_envio, forma_pago, calcular_pais(codigo_postal))
    
    with open(archivo_binario, 'ab') as binfile:
        pickle.dump(envio, binfile)

    print(f"Datos agregados al archivo binario '{archivo_binario}'.")



def es_letra(caracter):
    return 'A' <= caracter <= 'Z' or 'a' <= caracter <= 'z'

def es_digito(caracter):
    return '0' <= caracter <= '9'

def calcular_pais(cp):
    n = len(cp)

    if n < 4 or n > 9:
        return 'Otro'

    if n == 8:
        if es_letra(cp[0]) and cp[0] != 'I' and cp[0] != 'O':
            if es_digito(cp[1]) and es_digito(cp[2]) and es_digito(cp[3]) and es_digito(cp[4]):
                if es_letra(cp[5]) and es_letra(cp[6]) and es_letra(cp[7]):
                    return 'Argentina'
    
    elif n == 4:
        if es_digito(cp[0]) and es_digito(cp[1]) and es_digito(cp[2]) and es_digito(cp[3]):
            return 'Bolivia'
    
    elif n == 9:
        if es_digito(cp[0]) and es_digito(cp[1]) and es_digito(cp[2]) and es_digito(cp[3]):
            if es_digito(cp[4]) and cp[5] == '-':
                if es_digito(cp[6]) and es_digito(cp[7]) and es_digito(cp[8]):
                    return 'Brasil'

    elif n == 7:
        if es_digito(cp[0]) and es_digito(cp[1]) and es_digito(cp[2]) and es_digito(cp[3]):
            if es_digito(cp[4]) and es_digito(cp[5]) and es_digito(cp[6]):
                return 'Chile'

    elif n == 6:
        if es_digito(cp[0]) and es_digito(cp[1]) and es_digito(cp[2]) and es_digito(cp[3]):
            if es_digito(cp[4]) and es_digito(cp[5]):
                return 'Paraguay'

    elif n == 5:
        if es_digito(cp[0]) and es_digito(cp[1]) and es_digito(cp[2]):
            if es_digito(cp[3]) and es_digito(cp[4]):
                return 'Uruguay'

    return 'Otro'

def busqueda_codigo_postal(archivo_binario, codigo_postal):
    cantidad=0
    with open(archivo_binario, 'rb') as binfile:
        try:
            while True:
                envio = pickle.load(binfile)
                if envio.codigo == codigo_postal:
                    cantidad +=1
                    print(f"Envío encontrado: {envio.mostrar()}")
        except EOFError:
            pass  

    print(f"Cantidad encontrada {cantidad}")

def busqueda_direccion(archivo_binario, direccion):
    with open(archivo_binario, 'rb') as binfile:
        try:
            while True:
                envio = pickle.load(binfile)
                if envio.direccion == direccion:
                    return print(f"Envío encontrado: {envio.mostrar()}")
        except EOFError:
            pass  

    return print("No lo encontramos.")