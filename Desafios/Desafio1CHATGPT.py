def convertir_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

def convertir_tiempo(horas, minutos, segundos):
    segundos_totales = horas * 3600 + minutos * 60 + segundos
    return segundos_totales

def main():
    try:
        for _ in range(4):
            opcion = input("¿Desea convertir segundos a tiempo (s) o tiempo a segundos (t)? ").lower()
            if opcion == 's':
                segundos = int(input("Ingrese la cantidad de segundos transcurridos: "))
                if segundos < 0:
                    print("Por favor, ingrese un número entero positivo.")
                    continue
                
                horas, minutos, segundos_restantes = convertir_segundos(segundos)
                
                if horas <= 24:
                    print(f"Tiempo transcurrido: {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")
                else:
                    print("Excedido")
            elif opcion == 't':
                horas = int(input("Ingrese la cantidad de horas: "))
                minutos = int(input("Ingrese la cantidad de minutos: "))
                segundos = int(input("Ingrese la cantidad de segundos: "))

                if horas < 0 or minutos < 0 or segundos < 0:
                    print("Por favor, ingrese valores positivos.")
                    continue

                segundos_totales = convertir_tiempo(horas, minutos, segundos)
                print(f"Segundos totales transcurridos: {segundos_totales} segundos.")
            else:
                print("Por favor, seleccione 's' o 't'.")

    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
