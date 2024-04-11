accion = int(
    input(
        "Ingrese alguna opcion: \n \t 1- Segundos a tiempo(hh:mm:ss) \n \t 2- Tiempo(hh:mm:ss) a segundos \n"
    )
)
if accion == 1:
    segundos = int(input("Ingrese la cantidad de segundos: "))
    minutos = segundos // 60
    horas = minutos // 60

    segundos = segundos - minutos * 60
    minutos = minutos - horas * 60

    if horas < 25:
        print(f"{horas}:{minutos}:{segundos}")
    else:
        print("Excedido")
elif accion == 2:
    horas = int(input("Ingrese la cantidad de horas: "))
    minutos = int(input("Ingrese la cantidad de minutos: "))
    segundos = int(input("Ingrese la cantidad de segundos: "))

    tiempo_segundos = segundos + minutos * 60 + horas * 3600
    print(f"Dan los siquientes segundos {tiempo_segundos}")
else:
    print("Accion no permitida")
