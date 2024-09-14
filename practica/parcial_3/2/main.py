from clase import Publicacion

def mostrar_menu():
    print('bla bla')

def validar(tipo):
    return 1 <= tipo <=30
def opcion_1(lista):
    codigo= input('Ingrse el codgio: ')
    titulo= input('Ingrse el titulo: ')
    tipo= int(input('Ingrese el tipo(1-30): '))
    if not validar(tipo):
        return print('Tipo no permitido')
    try:
        costo=int(input('Ingrese el costo'))
    except:
        return print('Costo no permitido')
    publicacion=Publicacion(codigo,titulo,tipo,costo)
    lista.append(publicacion)    

def filtrar(lista,num):
    lista_filtrada=[]
    for i in lista:
        if i.costo > num:
            lista_filtrada.append(i)
    return lista_filtrada

def ordenar(lista):
    n=len(lista)
    for i in range(n-1):
        for j in range(i, n):
            if lista[i].codigo > lista[j].codigo:
                lista[i],lista[j]=lista[j],lista[i]
    return lista

def opcion_2(lista):
    num=int(input('Costo para filtrar: '))
    lista_filtrada=filtrar(lista,num)
    lista_ordenada= ordenar(lista_filtrada)
    
    for i in lista_ordenada:
        print(i)
    print(f'Promedio: {sum(lista_ordenada) // len(lista_ordenada)}')

def publicacion_tipo(lista):
    contador= [0] * 30
    for i in range(len(lista)):
        contador[lista[i].tipo - 1] += 1
    return contador

def opcion_3(lista):
    valor=int(input('Ingrese valor: '))
    lista_contador=publicacion_tipo(lista)
    for i in lista_contador:
        if i > valor:
            print(f'El tipo {i} tiene mas de {valor} publicaciones')

def principal():
    publicaciones=[]
    opcion= 0
    opciones=[opcion_1, opcion_2, opcion_3]
    while opcion != 5:
        mostrar_menu()
        opcion= int(input('Ingrese la opcion: '))
        if 1 <= opcion <= 4:
            opciones[opcion -1](publicaciones)



if __name__ == '__main__':
    principal()