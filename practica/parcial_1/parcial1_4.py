#Importaciones de librerias externas
import random
from statistics import mean

#Funcion para comprobacion
def comprobacion(variable1, variable2):
    return variable1 == variable2


#Semilla para el random
random.seed(789456)

#Variables necesarias
multiplos_3 = 0
multiplos_7 = 0
multiplos_no_3_7 = 0
menor_numero = None
suma_promedio = 0
n_promedio = 0
n_menores15 = 0
suma_numeros = 0

#Listas de comrpobacion
lista_menores = []
lista_promedio = []
lista_suma = []

#Bucle del 0 al 35000
for i in range(35000):
    #Generacion de numeros aleatorios
    numero_aleatorio = random.randint(1, 60000)
    
    #Ejercicio 1
    if numero_aleatorio % 3 == 0:
        multiplos_3 += 1
    elif numero_aleatorio % 7 == 0:
        multiplos_7 += 1
    else:
        multiplos_no_3_7 += 1

    #Ejercicio 2
    if numero_aleatorio % 10 in (1, 3, 7):
        if menor_numero is None or numero_aleatorio < menor_numero:
            lista_menores.append(numero_aleatorio)
            menor_numero = numero_aleatorio

    #Ejercicio 3
    if numero_aleatorio % 2 != 0 and numero_aleatorio > 30000:
        lista_promedio.append(numero_aleatorio)
        suma_promedio += numero_aleatorio
        n_promedio += 1

    #Ejercicio 4
    if numero_aleatorio < 15000:
        n_menores15 += 1

    #Ejercicio 5
    if numero_aleatorio % 9 == 0 and numero_aleatorio % 12 != 0:
        lista_suma.append(numero_aleatorio)
        suma_numeros += numero_aleatorio

#Calculos auxiliares
promedio = suma_promedio // n_promedio if n_promedio > 0 else 0
porcentaje = (n_menores15 * 100) // 35000


#Muestro los resultados y comprobaciones
print(
    f"Ejercicio 1: multiplo de 3: {multiplos_3} \n\t multiplo de 7: {multiplos_7} \n\t multiplos de otros: {multiplos_no_3_7}"
)
print(
    f"Ejercicio 2: menor numero: {menor_numero} -- comprobacion {comprobacion(min(lista_menores), menor_numero)}"
)
print(
    f"Ejercicio 3: promedio: {promedio} -- comprobacion {comprobacion(int(mean(lista_promedio)), promedio)}"
)
print(f"Ejercicio 4: porcentaje: {porcentaje}")
print(
    f"Ejercicio 5: suma: {suma_numeros} -- comprobacion {comprobacion(sum(lista_suma), suma_numeros)}"
)
