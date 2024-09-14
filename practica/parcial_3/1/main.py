from clase import Ticket
def cargar_menu():
    print('1- Cargar datos 2-Mostrar datos 3- Importe acumulado 4-Buscador')

def es_numero(numero):
    try:
        int(numero)
        return True
    except:
        return False

def compriobar_pais(pais):
    try:    
        pais_numero=int(pais)
        if 1 <= pais_numero <= 20:
            return True
        else:
            return False
    except:
        return False

def opcion_1(lista):
    codigo_vuelo= input('Ingrese el codigo del vuelo: ')
    numero_pasajero= input('Ingrese el identificador del pasajero: ')
    if not es_numero(numero_pasajero):
        return print('Identificador del pasajero incorrecto')
    pais_destino= input('Ingrese el pais de destino(numero del 1 al 20): ')
    if not compriobar_pais(pais_destino):
        return print('Pais de destino incorrecto')
    
    numero_asiento= input('Ingrese el numero asiento del pasajero: ')
    if not es_numero(numero_asiento):
        return print('numero asiento del pasajero incorrecto')
    
    importe= input('Ingrese el importe: ')
    if not es_numero(importe):
        return print('importe incorrecto')

    ticket=Ticket(codigo_vuelo,numero_pasajero,pais_destino,numero_asiento, importe)
    lista.append(ticket)

def filtrar_datos(lista,num):
    lista_filtrada=[]
    for i in lista:
        if int(i.numero_asiento) > num:
            lista_filtrada.append(i)
    return lista_filtrada

def ordenar(lista):
    n=len(lista)
    for i in range(n-1):
        for j in range(i,n):
            if lista[i].codigo_vuelo > lista[j].codigo_vuelo:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

def opcion_2(lista):
    num=int(input('Ingrese el valor para filtrar: '))
    lista_filtrada=filtrar_datos(lista,num)
    for i in ordenar(lista_filtrada):
        print(i)

def determinar_importe(lista):
    contadores=[0]*20
    for i in range(len(lista)):
        contadores[int(lista[i].pais_destino) - 1] += int(lista[i].importe)
    return contadores

def opcion_3(lista):
    valor= int(input('ingrese el valor: '))
    lista_importe_acumulado= determinar_importe(lista)
    for i in range(len(lista_importe_acumulado)):
        if int(lista_importe_acumulado[i]) > valor:
            print(f'Importes en pais {i+1}  {lista_importe_acumulado[i]}')

def opcion_4(lista):
    id= input('Numero de id a buscar: ')
    for i in lista:
        if i.numero_pasajero == id:
            print(i.numero_asiento + i.pais_destino)
            return 
    print('No lo encontramos')

def principal():
    tickets=[]
    opciones=[opcion_1,opcion_2, opcion_3, opcion_4]
    opcion= 0
    while opcion != '10':
        cargar_menu()   
        opcion = input('Ingrese una opcion: ')
        if es_numero(opcion) and 1 <= int(opcion) <= 4:
            opciones[int(opcion)-1](tickets)
        else:
            print('Opcion invalida')


if __name__ == '__main__':
    principal()