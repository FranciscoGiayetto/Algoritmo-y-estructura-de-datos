import pickle
import os

def mostrar_archivo(FD):
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe...')
        print()
        return
    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')

    print('Contenido del archivo', FD, '...')
    while m.tell() < tbm:
        vot = pickle.load(m)
        print(vot.mostrar())

    m.close()
    print()


mostrar_archivo('envios.pkg')