lista= [2,1,4,6,536,3,4,5,6,7]

def ordenar(lista):
    largo= len(lista)
    medio= largo//2
    while medio >0:
        for i in range(medio,largo):
            temp= lista[i]
            j=i
            while j>=medio and lista[j-medio]>temp:
                lista[j]= lista[j-medio]
                j -= medio
            lista[j]= temp
        medio //= 2

    print(lista)
    return lista

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return 'encontrado'
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return 'No enconctrado'


lista_ordenada=ordenar(lista)
print(busqueda_binaria(lista_ordenada,100))
