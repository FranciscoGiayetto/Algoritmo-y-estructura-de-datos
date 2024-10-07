import os
import pickle
from clase import Envio


def son_numeros(cadena):
    for letra in cadena:
        if letra not in ("0123456789"):
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
    print("6 - Determinar y mostrar la cantidad de envíos por tipo y forma de pago")
    print("7 - Totalizar envíos por tipo de envío y forma de pago")
    print("8 - Calcular importe promedio y listar envíos por encima del promedio")
    print("9 - Salir")
    print("=" * 40 + "\n")


def obtener_opcion():
    return input("Por favor, elige una opción: ")


def confirmar_eliminar_archivo():
    confirmacion = input(
        "Advertencia: el archivo binario existente será eliminado. ¿Desea continuar? (s/n): "
    )
    return confirmacion.lower() == "s"


def crear_archivo_binario(archivo_csv, archivo_binario):
    if not os.path.exists(archivo_csv):
        print(f"Error: El archivo '{archivo_csv}' no existe.")
        return

    if not confirmar_eliminar_archivo():
        print("Operación cancelada.")
        return

    if os.path.exists(archivo_binario):
        os.remove(archivo_binario)

    file_csv = open(archivo_csv, "r")
    file_csv.readline()
    file_csv.readline()

    file_binario = open(archivo_binario, "wb")

    for linea in file_csv:
        row = linea.strip().split(",")
        destino = calcular_pais(row[0])
        envio = Envio(
            codigo=row[0],
            direccion=row[1],
            tipo=row[2],
            forma_pago=row[3],
            pais=destino,
            importe=calcular_importe(destino, row[0], int(row[3]), int(row[2])),
        )
        pickle.dump(envio, file_binario)

    file_csv.close()
    file_binario.close()

    print(f"Archivo binario '{archivo_binario}' creado con éxito.")


def mostrar_contenido_binario(archivo_binario):
    print("\nContenido del archivo binario:")
    binfile = open(archivo_binario, "rb")

    while True:
        try:
            envio = pickle.load(binfile)
            print(envio.mostrar())
        except EOFError:
            break

    binfile.close()


def opcion_1(archivo_binario):
    archivo_csv = "envios-tp4.csv"
    crear_archivo_binario(archivo_csv, archivo_binario)
    return archivo_binario


def opcion_2(archivo_binario):
    carga_teclado(archivo_binario)


def opcion_3(archivo_binario):
    mostrar_contenido_binario(archivo_binario)


def opcion_4(archivo_binario):
    codigo_buscar = input("Ingrese el codigo postal a buscar: ")
    busqueda_codigo_postal(archivo_binario, codigo_buscar)


def opcion_5(archivo_binario):
    direccion = input("Ingrese la direccion a buscar: ")
    busqueda_direccion(archivo_binario, direccion)


def normalizacion_codigo_postal(codigo_postal):
    codigo_postal_sin_espacios = ""
    for i in codigo_postal:
        if i != " ":
            codigo_postal_sin_espacios += i
    return codigo_postal_sin_espacios


def verificacion_envio(tipo_envio):
    if tipo_envio in (0, 1, 2):
        return "Carta simple"
    elif tipo_envio in (3, 4):
        return "Carta certificada"
    else:
        return "Carta express"


def validacion_tipo_envio(tipo_envio):
    if tipo_envio in (0, 1, 2, 3, 4, 5, 6):
        return True
    else:
        return False


def veiificacion_forma_pago(valor):
    return valor in [1, 2]


def carga_teclado(archivo_binario):
    codigo_postal = normalizacion_codigo_postal(input("Ingrese el código postal: "))
    direccion = input("Ingrese la dirección: ")
    continuar = True

    while continuar:
        tipo_envio = int(
            input(
                "------------------\n"
                "0 - Carta Simple\n"
                "1 - Carta Simple\n"
                "2 - Carta Simple\n"
                "3 - Carta Certificada\n"
                "4 - Carta Certificada\n"
                "5 - Carta Expresa\n"
                "6 - Carta Expresa\n"
                "------------------\n"
                "Ingrese el tipo de envío (0-6):"
            )
        )
        if validacion_tipo_envio(tipo_envio):
            continuar = False
        else:
            print("\033[1m El tipo de envío no es válido\033[0m")
    continuar = True
    while continuar:
        forma_pago = int(
            input("Ingrese la forma de pago (1-efectivo, 2-tarjeta de crédito): ")
        )
        if veiificacion_forma_pago(forma_pago):
            continuar = False
        else:
            print("\033[1m La forma de pago no es válida\033[0m")

    destino = calcular_pais(codigo_postal)
    envio = Envio(
        codigo_postal,
        direccion,
        tipo_envio,
        forma_pago,
        destino,
        calcular_importe(destino, codigo_postal, forma_pago, tipo_envio),
    )

    binfile = open(archivo_binario, "ab")

    pickle.dump(envio, binfile)

    binfile.close()

    print(f"Datos agregados al archivo binario '{archivo_binario}'.")


def es_letra(caracter):
    return "A" <= caracter <= "Z" or "a" <= caracter <= "z"


def es_digito(caracter):
    return "0" <= caracter <= "9"


def calcular_pais(cp):
    n = len(cp)

    if n < 4 or n > 9:
        return "Otro"

    if n == 8:
        if es_letra(cp[0]) and cp[0] != "I" and cp[0] != "O":
            if (
                es_digito(cp[1])
                and es_digito(cp[2])
                and es_digito(cp[3])
                and es_digito(cp[4])
            ):
                if es_letra(cp[5]) and es_letra(cp[6]) and es_letra(cp[7]):
                    return "Argentina"

    elif n == 4:
        if (
            es_digito(cp[0])
            and es_digito(cp[1])
            and es_digito(cp[2])
            and es_digito(cp[3])
        ):
            return "Bolivia"

    elif n == 9:
        if (
            es_digito(cp[0])
            and es_digito(cp[1])
            and es_digito(cp[2])
            and es_digito(cp[3])
        ):
            if es_digito(cp[4]) and cp[5] == "-":
                if es_digito(cp[6]) and es_digito(cp[7]) and es_digito(cp[8]):
                    return "Brasil"

    elif n == 7:
        if (
            es_digito(cp[0])
            and es_digito(cp[1])
            and es_digito(cp[2])
            and es_digito(cp[3])
        ):
            if es_digito(cp[4]) and es_digito(cp[5]) and es_digito(cp[6]):
                return "Chile"

    elif n == 6:
        if (
            es_digito(cp[0])
            and es_digito(cp[1])
            and es_digito(cp[2])
            and es_digito(cp[3])
        ):
            if es_digito(cp[4]) and es_digito(cp[5]):
                return "Paraguay"

    elif n == 5:
        if es_digito(cp[0]) and es_digito(cp[1]) and es_digito(cp[2]):
            if es_digito(cp[3]) and es_digito(cp[4]):
                return "Uruguay"

    return "Otro"


def calcular_importe(pais, codigo, forma_pago, tipo):
    importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    monto = importes[tipo]
    if pais == "Argentina":
        inicial = monto
    else:
        if (
            pais == "Bolivia"
            or pais == "Paraguay"
            or (pais == "Uruguay" and codigo[0] == "1")
        ):
            inicial = int(monto * 1.20)
        elif pais == "Chile" or (pais == "Uruguay" and codigo[0] != "1"):
            inicial = int(monto * 1.25)
        elif pais == "Brasil":
            if codigo[0] == "8" or codigo[0] == "9":
                inicial = int(monto * 1.20)
            else:
                if (
                    codigo[0] == "0"
                    or codigo[0] == "1"
                    or codigo[0] == "2"
                    or codigo[0] == "3"
                ):
                    inicial = int(monto * 1.25)
                else:
                    inicial = int(monto * 1.30)
        else:
            inicial = int(monto * 1.50)

    final = inicial
    if forma_pago == 1:
        final = int(0.9 * inicial)

    return final


def busqueda_codigo_postal(archivo_binario, codigo_postal):
    cantidad = 0
    binfile = open(archivo_binario, "rb")

    while True:
        try:
            envio = pickle.load(binfile)
            if envio.codigo == codigo_postal:
                cantidad += 1
                print(f"Envío encontrado: {envio.mostrar()}")
        except EOFError:
            break

    binfile.close()
    print(f"Cantidad encontrada {cantidad}")


def busqueda_direccion(archivo_binario, direccion):
    binfile = open(archivo_binario, "rb")
    while True:
        try:
            envio = pickle.load(binfile)
            if envio.direccion == direccion:
                binfile.close()
                return print(f"Envío encontrado: {envio.mostrar()}")
        except EOFError:
            break

    binfile.close()
    return print("No lo encontramos.")


def total_envios(matriz_contadores, tipos_envio, formas_pago):
    print("\nTotal de envíos por tipo de envío:")
    for i in range(len(tipos_envio)):
        total_fila = 0
        for j in range(len(formas_pago)):
            total_fila += matriz_contadores[i][j]
        print(f"Tipo {i}({tipos_envio[i]}): {total_fila}")

    print("\nTotal de envíos por forma de pago:")
    for j in range(len(formas_pago)):
        total_columna = 0
        for i in range(len(tipos_envio)):
            total_columna += matriz_contadores[i][j]
        print(f"{formas_pago[j]}: {total_columna}")


def generar_matriz(archivo_binario):
    matriz_contadores = [[0 for _ in range(2)] for _ in range(7)]
    tipos_envio = [
        "Carta Simple",
        "Carta Simple",
        "Carta Simple",
        "Carta Certificada",
        "Carta Certificada",
        "Carta Expresa",
        "Carta Expresa",
    ]
    formas_pago = ["Efectivo", "Tarjeta de credito"]

    binfile = open(archivo_binario, "rb")

    while True:
        try:
            envio = pickle.load(binfile)
            tipo = int(envio.tipo)
            forma_pago = int(envio.forma_pago)

            matriz_contadores[tipo][forma_pago - 1] += 1
        except EOFError:
            break

    binfile.close()

    return matriz_contadores, tipos_envio, formas_pago


def opcion_6(archivo_binario):
    matriz_contadores, tipos_envio, formas_pago = generar_matriz(archivo_binario)
    print("\nCantidad de envíos por tipo y forma de pago:")
    for i in range(len(tipos_envio)):
        for j in range(len(formas_pago)):
            if matriz_contadores[i][j] > 0:
                print(
                    f"Tipo {i}({tipos_envio[i]}) - {formas_pago[j]}: {matriz_contadores[i][j]}"
                )
    return matriz_contadores, tipos_envio, formas_pago


def opcion_7(archivo_binario, matriz_contadores, tipos_envio, formas_pago):
    total_envios(matriz_contadores, tipos_envio, formas_pago)


def add_in_order(arreglo, envio):
    n = len(arreglo)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if arreglo[c].codigo == envio.codigo:
            pos = c
            break

        if envio.codigo < arreglo[c].codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    arreglo[pos:pos] = [envio]


def get_importes_mayores(archivo_binario, condicion):
    lista_envios = []

    if not os.path.exists(archivo_binario):
        print("El archivo", archivo_binario, "no existe...")
        print()
        return

    tbm = os.path.getsize(archivo_binario)
    m = open(archivo_binario, "rb")
    print("Creando el arreglo desde el archivo", archivo_binario, "...")
    while m.tell() < tbm:
        envio = pickle.load(m)
        if envio.importe > condicion:
            add_in_order(lista_envios, envio)
    m.close()
    print("... hecho")
    print()

    return lista_envios


def opcion_8(archivo_binario):
    promedio = [0, 0, 0]

    if not os.path.exists(archivo_binario):
        print("El archivo", archivo_binario, "no existe...")
        print()
        return

    tbm = os.path.getsize(archivo_binario)
    m = open(archivo_binario, "rb")
    print("Creando el arreglo desde el archivo", archivo_binario, "...")
    while m.tell() < tbm:
        envio = pickle.load(m)
        promedio[0] += envio.importe
        promedio[1] += 1

    promedio[2] = promedio[0] / promedio[1]
    m.close()
    print("Promedio calculado satisfactoriamente:", promedio[2])
    for i in get_importes_mayores(archivo_binario, promedio[2]):
        print(i.mostrar())
