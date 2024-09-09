class Alumno():
    def __init__(self,dni_alumno,nombre_alumno,apellido_alumno,dni_tutor,nivel,importe_cuota):
        self.dni_alumno= dni_alumno
        self.nombre_alumno= nombre_alumno
        self.apellido_alumno= apellido_alumno
        self.dni_tutor= dni_tutor
        self.importe_cuota= importe_cuota
        self.nivel=nivel
    def mostrar(self):
        return (f"Alumno: {self.nombre_alumno} {self.apellido_alumno} / "
            f"DNI del Alumno: {self.dni_alumno} / "
            f"DNI del Tutor: {self.dni_tutor} / "
            f"Nivel: {self.nivel} / "
            f"Importe de la Cuota: {self.importe_cuota}")
        
def mostrar_menu():
    print("0. Salir")
    print("1. Registrar alumno")
    print("2. Mostrar alumnos ordenados")
    print("3. Mostrar alumnos por nivel")
    print("4. Mostrar alumnos por importe de la cuota")

def comprobacion_nivel(nivel):
    return 0 <= nivel >= 12

def opcion_1(lista):
    dni_alumno=input("Ingrese el DNI del alumno: ")
    nombre_alumno=input("Ingrese el nombre del alumno: ")
    apellido_alumno=input("Ingrese el apellido del alumno: ")
    dni_tutor=input('Ingrese el dni del tutor: ')
    continuar=True
    while continuar:
        nivel=int(input("Ingrese el nivel del alumno: "))
        if not comprobacion_nivel(nivel):
            continuar= False
        else:
            print('nivel no permitido')
    importe_cuota=input("Ingrese el importe de la cuota: ")

    alumno= Alumno(dni_alumno,nombre_alumno,apellido_alumno,dni_tutor,nivel,importe_cuota)
    lista.append(alumno)

def opcion_2(lista):
    n = len(lista)
    h = 1
    # Calcular el valor inicial de h
    while h < n // 3:
        h = 3 * h + 1
    
    # Shell Sort
    while h > 0:
        for j in range(h, n):
            y = lista[j].apellido_alumno
            k = j - h
            while k >= 0 and y < lista[k].apellido_alumno:
                lista[k + h].apellido_alumno = lista[k].apellido_alumno
                k -= h
            lista[k + h].apellido_alumno = y
        h //= 3  # Reducir h
    
    # Mostrar elementos ordenados
    for i in lista:
        print(i.mostrar())
        print('---------')
    return lista

def opcion_3(lista):
    alumnos_nivel=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(lista)):
        alumnos_nivel[i] +=1
    
    for i in range(len(alumnos_nivel)):
        print('Nivel ',i , alumnos_nivel[i])

def opcion_4(lista):
    dni_buscar=input('Ingrese el dni del tutor a buscar: ')
    importe_total=0
    for i in range(len(lista)):
        if lista[i].dni_tutor==dni_buscar:
            importe_total += int(lista[i].importe_cuota)
    print('total a pagar: ', importe_total)

def opcion_5(lista):
    dni_buscar=input('Ingrese el dni del niño a buscar: ')
    encontrado=True
    for i in range(len(lista)):
        if lista[i].dni_alumno==dni_buscar:
            lista[i].importe_cuota = int(lista[i].importe_cuota)-int(lista[i].importe_cuota) * 0.10
            print(lista[i].mostrar())
            encontrado=False
            break
    if encontrado:
        print('El niño no se encuentra en la lista')

            

def principal():
    alumnos=[]
    opciones= [opcion_1, opcion_2, opcion_3,opcion_4,opcion_5]
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))
        if 1 <= opcion <= 6:
            if opcion == 3:
                opciones[opcion - 1](alumnos_ordenado)
            else:
                alumnos_ordenado=opciones[opcion - 1](alumnos)

        elif opcion == 0:
            continuar = False
        else:
            print("Opción no válida")

if __name__ == '__main__':
    principal()