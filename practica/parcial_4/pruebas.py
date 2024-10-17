def ordenar_lista(lista,objeto):
    longitud= len(lista)
    posicion= longitud
    izquierda= 0
    derecha= longitud-1
    while izquierda <= derecha:
        medio= (derecha+izquierda)//2
        if lista[medio] == objeto:
            posicion= medio
            break
        if lista[medio] > objeto:
            derecha = medio - 1
        else:
            izquierda = medio + 1
        
        if izquierda > derecha:
            posicion= izquierda
    lista[posicion:posicion]= [objeto]

lista=[]
ordenar_lista(lista,8)
ordenar_lista(lista,4)
ordenar_lista(lista,10)
print(lista)