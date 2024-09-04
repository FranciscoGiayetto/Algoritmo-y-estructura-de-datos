from envios import Envio

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


def mostrar_r2_r3(parametro1, parametro2):
    print(' (r2) - Cantidad de envios con direccion valida:', parametro1)
    print(' (r3) - Cantidad de envios con direccion no valida:', parametro2)


def calcular_promedio_envios_ba(precio_total, cantidad_envios):
    if cantidad_envios != 0:
        return int(precio_total / cantidad_envios)
    else:
        return 0


def calcular_promedio_envios_internacionales(envios_totales, envios_internacionales):
    return int((100 * envios_internacionales) / envios_totales)


def calcular_tipo_mayor(contador_carta_simple, contador_carta_certificada, contador_carta_express):
    if contador_carta_simple > contador_carta_certificada and contador_carta_simple > contador_carta_express:
        return 'Carta simple'
    elif contador_carta_certificada > contador_carta_simple and contador_carta_certificada > contador_carta_express:
        return 'Carta certificada'
    elif contador_carta_simple == contador_carta_express or contador_carta_simple == contador_carta_certificada:
        return 'Carta simple'
    elif contador_carta_certificada == contador_carta_express:
        return 'Carta certificada'
    else:
        return 'Carta express'


def test_calculo(cp, tipo, pago):
    n = len(cp)
    envio_BA = False
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

    # 2. Determinación de la provincia del lugar de destino.
    if destino == 'Argentina':
        p = cp[0]
        if p == 'B':
            provincia = 'Buenos Aires'
            envio_BA = True
        elif p == 'I' or p == 'O':
            destino = 'Otro'

    # 3. Determinación del importe inicial a pagar.
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

    # 4. Determinación del valor final del ticket a pagar.
    # asumimos que es pago en tarjeta...
    final = inicial

    # ... y si no lo fuese, la siguiente será cierta y cambiará el valor...
    if pago == 1:
        final = int(0.9 * inicial)

    return final, destino, envio_BA


def cargar_datos_archivo():
    envios = open("envios-tp3.txt", "r", encoding="utf-8")
    flag = True
    control = ''
    codigo_postal = ''
    direccion = ''
    tipo_envio = None
    forma_pago = 0
    cantidad_control_valido = 0
    cantidad_control_invalido = 0
    contador_carta_simple = 0
    contador_carta_certificada = 0
    contador_carta_express = 0
    imp_acu_total = 0
    primer_cp = ''
    flag_primer_cp = True
    cant_primer_cp = 0
    menor_importe_brasil = None
    mencp = ''
    total_envios_BA = 0
    contador_envios_BA = 0
    flag_BA = False
    envios_exterior = 0
    precio = 0
    pais_del_codigo = ""
    control_valido = True
    envios_lista=[]
    for linea in envios:
        if flag:
            control = buscar_estructura_control(linea)
            flag = False
        else:
            codigo_postal = normalizacion_codigo_postal(linea[:9])
            if flag_primer_cp:
                primer_cp = codigo_postal
                flag_primer_cp = False
            if primer_cp == codigo_postal:
                cant_primer_cp += 1
            direccion = normalizacion_direccion(linea[9:28])

            if control == 'Hard Control':
                if hard_control(direccion):
                    cantidad_control_valido += 1
                    control_valido = True
                else:
                    cantidad_control_invalido += 1
                    control_valido = False
            else:
                cantidad_control_valido += 1

            tipo_envio = int(linea[29])
            forma_pago = int(linea[30])
            precio, pais_del_codigo, flag_BA = test_calculo(codigo_postal, tipo_envio, forma_pago)
            if control_valido:
                if tipo_envio is not None:
                    if verificacion_envio(tipo_envio) == 'Carta simple':
                        contador_carta_simple += 1
                    elif verificacion_envio(tipo_envio) == 'Carta certificada':
                        contador_carta_certificada += 1
                    else:
                        contador_carta_express += 1

                # Esto tiene que ser sin importar si es HC o SC

                imp_acu_total += precio
                if pais_del_codigo != "Argentina":
                    envios_exterior += 1

                if flag_BA:
                    contador_envios_BA += 1
                    total_envios_BA += precio

            if pais_del_codigo == 'Brasil':
                if menor_importe_brasil is None:
                    menor_importe_brasil = precio
                    mencp = codigo_postal
                elif precio < menor_importe_brasil:
                    menor_importe_brasil = precio
                    mencp = codigo_postal
            
            envio= Envio(codigo_postal,direccion,tipo_envio,forma_pago)
            envios_lista.append(envio)
    envios.close()
    return envios_lista

def carga_teclado():
    envios_lista=[]
    codigo_postal=normalizacion_codigo_postal(input('Ingrese el codigo postal'))
    direccion=normalizacion_direccion(input('Ingrese la direccion'))
    tipo_envio=input('Ingrese el tipo de envio')
    forma_pago=input('Ingrese la forma de pago')
    envio= Envio(codigo_postal,direccion,tipo_envio,forma_pago)
    envios_lista.append(envio)

    return envios_lista

def principal():
    i = 0
    if i == 0:
        lista_envios=[]
        i= 1
    opcion= input('1- Cargar datos del archivo /n 2- Cargar datos por teclado')
    if opcion == '1':
        confirmacion=input('Se eliminara la lista actual ¿quiere seguir? s/n')
        if confirmacion.lower() == 's':
            lista_envios=[]
            lista_envios=cargar_datos_archivo()
            print(lista_envios)
        else:
            print('No se cargaron datos')
    elif opcion == '2':
        carga_teclado()
        


if __name__ == '__main__':
    principal()