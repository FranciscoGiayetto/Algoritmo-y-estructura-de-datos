def matriz(lista):
    #columnas= lote filas= manzana
    matriz= [[0]*4 for j in range(35)]
    for i in range(len(lista)):
        fila= lista[i].manzana - 1
        columna=lista[i].orientacion -1 
        matriz[fila][columna] += lista[i].cantidad
    
    for fila in range(35):
        for columna in range(4):
            print('Columna: ', columna+1, 'Fila: ', fila+1, 'Cantidad: ',matriz[fila][columna])


def binario(lista,objeto):
    longitud= len(lista)
    posicion= longitud
    derecha= longitud - 1
    izquierda= 0
    while izquierda <= derecha:
        medio= (derecha + izquierda) // 2
        if lista[medio].isbn == objeto.isbn:
            posicion= medio
            break

        if lista[medio].isbn > objeto.isbn:
            derecha= medio - 1
        else:
            izquierda= medio + 1
    if izquierda > derecha:
        posicion= izquierda
    lista[posicion:posicion]=[objeto]