import Functions

def veiificacion_forma_pago(valor):
    return valor == 2 or valor == 1

def buscar_codigo_postal(lista,codigo):
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        codigo_postal_medio = lista[medio].codigo  # Accede al atributo 'codigo'
        
        if codigo_postal_medio == codigo:
            return lista[medio]  # Retorna el índice del código postal encontrado
        elif codigo_postal_medio < codigo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return False

def ordenar_menor_mayor(lista,cantidad,mostrar):
        
    n = len(lista)
    mitad = n // 2  # Inicia con la mitad del tamaño del arreglo

    # Reduce el gap hasta 0
    while mitad > 0:
        for i in range(mitad, n):
            temp = lista[i]  # Guarda el objeto completo
            j = i
            while j >= mitad and lista[j - mitad].codigo > temp.codigo:
                lista[j] = lista[j - mitad]  # Mueve el objeto completo
                j -= mitad

            lista[j] = temp  # Inserta el objeto en su lugar correcto

        mitad //= 2
    if mostrar == True:
        if cantidad == 0:
            for item in lista:
                print(item.codigo)
        else:
            for item in range(0,cantidad):
                print(lista[item].codigo)
            
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
    if tipo_envio in (0,1,2,3,4,5,6):
        return True
    else:
        return False



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
            
            envio= Functions.Envio(codigo_postal,direccion,tipo_envio,forma_pago)
            envios_lista.append(envio)
    envios.close()
    return envios_lista

def carga_teclado():
    codigo_postal=normalizacion_codigo_postal(input('Ingrese el codigo postal'))
    direccion=normalizacion_direccion(input('Ingrese la direccion'))
    continuar= True

    while continuar:
        tipo_envio= int(input('Ingrese el tipo de envio del 0 al 6'))
        if validacion_tipo_envio(tipo_envio):
            continuar = False
        else:
            print('El tipo de envio no es valido')
    continuar = True
    while continuar:
        forma_pago = int(input('Ingrese la forma de pago(1-efectivo 2-tarjeta de credito)'))
        if veiificacion_forma_pago(forma_pago):
            continuar= False
        else:
            print('La forma de pago no es valida')

    envio= Functions.Envio(codigo_postal,direccion,tipo_envio,forma_pago)

    return envio


def buscar_direc_y_tp(lista_envios):
    resultado_envio = None
    bsqd_direccion = input('Ingrese la direccion del envio: ')
    continuar= True
    while continuar:
        bsqd_tipo_envio = int(input('Ingrese el tipo del envio: '))
        if validacion_tipo_envio(bsqd_tipo_envio):
            continuar = False
        else:
            print('El tipo de envio no es valido')
    
    for envio in lista_envios:
        if envio.direccion == bsqd_direccion and envio.tipo == bsqd_tipo_envio:
            resultado_envio = envio.mostrar()
            break
            
    if resultado_envio is not None:
        print(f"El resultado de la busqueda es: {resultado_envio}")
    else:
        print("No existe ningun envio que coincida con la busqueda")
        
    return

def principal():
    lista_envios=[]
    opcion=0
    while opcion != '10':
        opcion= input('1- Cargar datos del archivo \n 2- Cargar datos por teclado \n 3-Mostrar registros \n 4-Buscar envio por direccion y tipo de envio \n 5- buscar codigo postal \n 9- calcular y mostrar importe final del envio \n 10- Salir')
        #dos vectorr y funciones
        if opcion == '1':
            confirmacion=input('Se eliminara la lista actual ¿quiere seguir? s/n')
            if confirmacion.lower() == 's':
                lista_envios=[]
                lista_envios=cargar_datos_archivo()
            else:
                print('No se cargaron datos')

        elif opcion == '2':
            lista_envios.append(carga_teclado())
            print(lista_envios)

        elif opcion == '3':
            decision=int(input('Si quiere mostrar todos ponga 0, sino el numero de la cantidad de registros'))
            lista_envios=ordenar_menor_mayor(lista_envios,decision,True)
        
        elif  opcion == '4':
            if lista_envios != []:
                buscar_direc_y_tp(lista_envios)
            else:
                print('No existen envios cargados, cargar envios para realizar la busqueda')
        
        elif opcion == '5':
            codigo=input('ingrese el codigo posta a buscar: ')

            envio= buscar_codigo_postal(ordenar_menor_mayor(lista_envios,0,False),codigo)
            if envio is not False:
                print('Lo hemos encontrado')
                print(envio.mostrar(), 'Antes')
                if envio.forma_pago == '1':
                    envio.forma_pago = 2
                else:
                    envio.forma_pago = 1
                
                print(envio.mostrar(), 'Despues')
            else:
                print('No encontrado')
        elif opcion == '9':
            suma=0
            cantidad=0
            contador=0
            for item in lista_envios:
                cantidad += 1
                suma += test_calculo(item.codigo,item.tipo,item.forma_pago)[0]
            promedio= suma // cantidad
            for item in lista_envios:
                if test_calculo(item.codigo,item.tipo,item.forma_pago)[0] < promedio:
                    contador +=1
            print(suma, cantidad)
            print(promedio, 'cantidad menores al promedio ', contador)
            

        


if __name__ == '__main__':
    principal()