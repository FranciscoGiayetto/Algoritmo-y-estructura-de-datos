n=int(input('Ingrese n: '))

tamano_orbita= 0
numero_mayor=None
suma_n= 0
lista_n=[]

while n != 1:
    suma_n += n
    tamano_orbita +=1
    lista_n.append(int(n))

    if numero_mayor == None or n > numero_mayor:
        numero_mayor=n

    if n % 2 == 0:
        n = n/2
    else:
        n= 3*n +1
else:
    lista_n.append(int(n))
    suma_n += n
    tamano_orbita +=1


print(f'Lista de n: {lista_n}')
print(f'El tamaño de la orbita es: {tamano_orbita}')
print(f'El numero mayor es: {numero_mayor}, max lista {max(lista_n)}')
print(f'Promedio de n es: {suma_n / tamano_orbita}')