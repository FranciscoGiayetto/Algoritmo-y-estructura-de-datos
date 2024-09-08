class Envio:
    def __init__(self, codigo, direccion, tipo, forma_pago):
        self.codigo = codigo
        self.direccion = direccion
        self.tipo = tipo
        self.forma_pago = forma_pago

    def get_importe(self):
        return calcular_importe(self.codigo, self.tipo, self.forma_pago)[0]

    def get_destino(self):
        return calcular_importe(self.codigo, self.tipo, self.forma_pago)[1]
    
    def mostrar(self):
        return f"Código: {self.codigo} / Dirección: {self.direccion}/ Tipo de envío {self.tipo} / Forma de Pago {self.forma_pago} / País: {self.get_destino()}"


def veiificacion_forma_pago(valor):
    return valor in [1, 2]


def buscar_codigo_postal(lista, codigo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        codigo_postal_medio = lista[medio].codigo

        if codigo_postal_medio == codigo:
            return lista[medio]
        elif codigo_postal_medio < codigo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return False


def ordenar_menor_mayor(lista, cantidad, mostrar):
    n = len(lista)
    mitad = n // 2

    while mitad > 0:
        for i in range(mitad, n):
            temp = lista[i]
            j = i
            while j >= mitad and lista[j - mitad].codigo > temp.codigo:
                lista[j] = lista[j - mitad]
                j -= mitad

            lista[j] = temp
        mitad //= 2

    if mostrar == True:
        if cantidad == 0:
            for item in lista:
                print(item.mostrar())
        else:
            for item in range(0, cantidad):
                print(lista[item].mostrar())

    return lista


def buscar_estructura_control(linea):
    for i in range(len(linea)):
        if linea[i: i + 2] == 'HC':
            return 'Hard Control'
        elif linea[i: i + 2] == 'SC':
            return 'Soft Control'


def son_numeros(cadena):
    for letra in cadena:
        if letra not in ('0123456789'):
            return False
    return True


def verificacion_mayusculas(cadena):
    if type(cadena) == int or cadena == ' ':
        return False
    return cadena == cadena.upper()


def hard_control(destino):
    numeros_letras = (
        ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I',
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    for i in range(len(destino)):
        if destino[i] in numeros_letras:
            if verificacion_mayusculas(destino[i]) and verificacion_mayusculas(destino[i + 1]):
                return False
            else:
                if destino[i] == ' ' and i + 1 < len(destino):
                    if son_numeros(destino[i + 1]):
                        if son_numeros(destino[i + 1:]):
                            return True
        else:
            return False
    return False


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


def calcular_importe(cp, tipo, pago):
    n = len(cp)
    if n < 4 or n > 9:
        destino = 'Otro'

    else:
        # ¿es Argentina?
        if n == 8:
            if 'A' <= cp[0] <= 'Z' and cp[0] != 'I' and cp[0] != 'O':
                if '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9' and '0' <= cp[4] <= '9':
                    if 'A' <= cp[5] <= 'Z' and 'A' <= cp[6] <= 'Z' and 'A' <= cp[7] <= 'Z':
                        destino = 'Argentina'
                    else:
                        destino = 'Otro'
                else:
                    destino = 'Otro'
            else:
                destino = 'Otro'

        else:
            # ¿es Bolivia?
            if n == 4:
                if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                    destino = 'Bolivia'
                else:
                    destino = 'Otro'

            else:
                # ¿es Brasil?
                if n == 9:
                    if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                        if '0' <= cp[4] <= '9' and cp[5] == '-':
                            if '0' <= cp[6] <= '9' and '0' <= cp[7] <= '9' and '0' <= cp[8] <= '9':
                                destino = 'Brasil'
                            else:
                                destino = 'Otro'
                        else:
                            destino = 'Otro'
                    else:
                        destino = 'Otro'

                else:
                    # ¿es Chile?
                    if n == 7:
                        if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                            if '0' <= cp[4] <= '9' and '0' <= cp[5] <= '9' and '0' <= cp[6] <= '9':
                                destino = 'Chile'
                            else:
                                destino = 'Otro'
                        else:
                            destino = 'Otro'
                    else:
                        # ¿es Paraguay?
                        if n == 6:
                            if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[
                                3] <= '9':
                                if '0' <= cp[4] <= '9' and '0' <= cp[5] <= '9':
                                    destino = 'Paraguay'
                                else:
                                    destino = 'Otro'
                            else:
                                destino = 'Otro'

                        else:
                            # ¿es Uruguay?
                            if n == 5:
                                if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9':
                                    if '0' <= cp[3] <= '9' and '0' <= cp[4] <= '9':
                                        destino = 'Uruguay'
                                    else:
                                        destino = 'Otro'
                                else:
                                    destino = 'Otro'
                            else:
                                destino = 'Otro'

    if destino == 'Argentina':
        p = cp[0]
        if p == 'I' or p == 'O':
            destino = 'Otro'

    importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    monto = importes[tipo]
    if destino == 'Argentina':
        inicial = monto
    else:
        if destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1'):
            inicial = int(monto * 1.20)
        elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1'):
            inicial = int(monto * 1.25)
        elif destino == 'Brasil':
            if cp[0] == '8' or cp[0] == '9':
                inicial = int(monto * 1.20)
            else:
                if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                    inicial = int(monto * 1.25)
                else:
                    inicial = int(monto * 1.30)
        else:
            inicial = int(monto * 1.50)

    final = inicial
    if pago == 1:
        final = int(0.9 * inicial)

    return final, destino


def cargar_datos_archivo():
    envios = open("envios-tp3.txt", "r", encoding="utf-8")
    flag = True
    control = ''
    codigo_postal = ''
    direccion = ''
    tipo_envio = None
    forma_pago = 0
    envios_lista = []
    for linea in envios:
        if flag:
            control = buscar_estructura_control(linea)
            flag = False
        else:
            codigo_postal = normalizacion_codigo_postal(linea[:9])
            direccion = normalizacion_direccion(linea[9:28])
            tipo_envio = int(linea[29])
            forma_pago = int(linea[30])

            envio = Envio(codigo_postal, direccion, tipo_envio, forma_pago)

            envios_lista.append(envio)
    envios.close()
    return envios_lista, control


def carga_teclado(lista_envios):
    codigo_postal = normalizacion_codigo_postal(input('Ingrese el código postal: '))
    direccion = normalizacion_direccion(input('Ingrese la dirección: '))
    continuar = True

    while continuar:
        tipo_envio = int(input(
            'Ingrese el tipo de envío (0-6):\n'
            '0 - Carta Simple\n'
            '1 - Carta Simple\n'
            '2 - Carta Simple\n'
            '3 - Carta Certificada\n'
            '4 - Carta Certificada\n'
            '5 - Carta Expresa\n'
            '6 - Carta Expresa\n'
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

    valido = False

    if not valido:
        valido = hard_control(direccion)
    envio = Envio(codigo_postal, direccion, tipo_envio, forma_pago)
    return envio


def buscar_direc_y_tp(lista_envios):
    resultado_envio = None
    bsqd_direccion = input('Ingrese la dirección del envío: ')
    continuar = True
    while continuar:
        bsqd_tipo_envio = int(input('Ingrese el tipo de envío: '))
        if validacion_tipo_envio(bsqd_tipo_envio):
            continuar = False
        else:
            print('\033[1m El tipo de envio no es valido \033[0m')

    for envio in lista_envios:
        if envio.direccion == bsqd_direccion and envio.tipo == bsqd_tipo_envio:
            resultado_envio = envio.mostrar()
            break

    if resultado_envio is not None:
        print(f"El resultado de la búsqueda es: {resultado_envio}")
    else:
        print("\033[1mNo existe ningun envio que coincida con la busqueda\033[0m")


def cantidad_de_envios_por_tipo(lista_envios, control):
    cont_envios_validos = [0, 0, 0, 0, 0, 0, 0]
    cont_importes_final = [0, 0, 0, 0, 0, 0, 0]
    for envio in lista_envios:
        if hard_control(envio.direccion) or control == 'Soft Control':
            cont_envios_validos[envio.tipo] += 1
            cont_importes_final[envio.tipo] += envio.get_importe()

    return cont_envios_validos, cont_importes_final


def mostrar_menu():
    print("\n" + "=" * 40)
    print("        MENÚ DE OPCIONES        ")
    print("=" * 40)
    print("1 - Cargar datos del archivo")
    print("2 - Cargar datos por teclado")
    print("3 - Mostrar registros")
    print("4 - Buscar envío por dirección y tipo de envío")
    print("5 - Buscar código postal")
    print("6 - Determinar cantidad de tipos de envíos")
    print("7 - Calcular importes finales por tipos")
    print("8 - Mostrar envio con mayor importe acumulado y porcentaje sobre total")
    print("9 - Calcular y mostrar importe final del envío")
    print("10 - Salir")
    print("=" * 40 + "\n")


def obtener_opcion():
    return input("Por favor, elige una opción: ")


def opcion_1(lista_envios, tipo_control):
    confirmacion = input('Se eliminará la lista actual ¿quiere seguir? s/n: ')
    if confirmacion.lower() == 's':
        lista_envios.clear()
        lista_envios.extend(cargar_datos_archivo()[0])
        print("\033[1m Datos cargados del archivo correctamente.\033[0m")
    else:
        print('\033[1m No se cargaron datos.\033[0m')
    return cargar_datos_archivo()[1]


def opcion_2(lista_envios, tipo_control):
    lista_envios.append(carga_teclado(lista_envios))
    print("\033[1mDatos cargados manualmente.\033[0m")


def opcion_3(lista_envios, tipo_control):
    decision = input('Si quiere mostrar todos los envíos ponga 0, sino el numero de la cantidad de registros que desea mostrar: ')
    if son_numeros(decision):
        lista_envios = ordenar_menor_mayor(lista_envios, int(decision), True)
    else:
        print("\033[1m Opción no válida, ingrese un número.\033[0m")


def opcion_4(lista_envios, tipo_control):
    if lista_envios:
        buscar_direc_y_tp(lista_envios)
    else:
        print('\033[1m No existen envíos cargados, cargar envíos para realizar la búsqueda. \033[0m')


def opcion_5(lista_envios, tipo_control):
    if lista_envios:
        codigo = input('Ingrese el codigo posta a buscar: ')
        envio = buscar_codigo_postal(ordenar_menor_mayor(lista_envios, 0, False), codigo)
        if envio is not False:
            print('\033[1m Lo hemos encontrado \033[0m')
            print(envio.mostrar(), 'Antes')
            if envio.forma_pago == '1':
                envio.forma_pago = 2
            else:
                envio.forma_pago = 1

            print(envio.mostrar(), 'Después')
        else:
            print('\033[1m No encontrado \033[0m')
    else:
        print('\033[1m No existen envíos cargados, cargar envíos para realizar la búsqueda. \033[0m')


def mostrar_envios_tipo(lista_envios, numero, control):
    if lista_envios:
        tipos = ['Carta Simple ', 'Carta Simple ', 'Carta Simple ',
                 'Carta Certificada ', 'Carta Certificada ',
                 'Carta Expresa ', 'Carta Expresa ']
        cantidad_envios = cantidad_de_envios_por_tipo(lista_envios, control)[numero]
        if numero == 0:
            print('Cantidad de envíos validos por tipo de envío')
            for i in range(len(tipos)):
                print(f'Tipo: ', i, ' cantidad: ', cantidad_envios[i])
        else:
            print('Suma total de importe por tipo de envío')
            for i in range(len(tipos)):
                print(f'Tipo: ', i, ' cantidad: $', cantidad_envios[i])


    else:
        print('\033[1m No existen envíos cargados, cargar envíos para realizar la búsqueda. \033[0m')


def opcion_6(lista_envios, tipo_control):
    mostrar_envios_tipo(lista_envios, 0, tipo_control)


def opcion_7(lista_envios, tipo_control):
    mostrar_envios_tipo(lista_envios, 1, tipo_control)


def determinar_maximo(lista_envios, tipo_control):
    lista = cantidad_de_envios_por_tipo(lista_envios, tipo_control)[1]
    return lista.index(max(lista))


def opcion_8(lista_envios, tipo_control):
    if lista_envios and cantidad_de_envios_por_tipo(lista_envios, tipo_control)[1]:
        tipo_maximo = determinar_maximo(lista_envios, tipo_control)
        porcentaje = max(cantidad_de_envios_por_tipo(lista_envios, tipo_control)[1]) / sum(
            cantidad_de_envios_por_tipo(lista_envios, tipo_control)[1])
        print(f'El tipo de envío con mayor cantidad de importes acumulados fue el Tipo {tipo_maximo}. Porcentaje: {int(porcentaje * 100)} %')

    else:
        print('\033[1m No existen envíos cargados, cargar envíos para realizar la búsqueda. \033[0m')


def opcion_9(lista_envios, tipo_control):
    suma = 0
    cantidad = 0
    contador = 0
    for item in lista_envios:
        cantidad += 1
        suma += item.get_importe()
    promedio = suma // cantidad if cantidad > 0 else 0
    for item in lista_envios:
        if item.get_importe() < promedio:
            contador += 1
    print('Promedio de importes de todos los envíos: $', promedio,
          '\nCantidad de envíos con importes menores al promedio: ', contador)
