def mostrar(n):
    if n < 0:
        return
    print('El número', n, 'es válido')


def test():
    n = int(input('Ingrese un número: '))
    mostrar(n)
    print('Programa terminado...')


# script principal
test()