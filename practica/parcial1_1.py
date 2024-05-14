import random
from math import trunc

random.seed(49)


multiplos_9 = 0
multiplos_5 = 0
multiplos_7 = 0
numero_mayor = 0
numero_par_menor = 0

for i in range(20000):
    # Genero numeros aleatorios
    numero_random = random.randint(1, 45000)

    # Ejercicio 1
    if numero_random % 5 == 0:
        multiplos_5 += 1
    if numero_random % 9 == 0:
        multiplos_9 += 1
    if numero_random % 7 == 0:
        multiplos_7 += 1

    # Ejercicio 2
    if numero_random % 10 >= 5 and numero_random % 10 <= 8:
        if numero_mayor < numero_random:
            numero_mayor = numero_random

    # Ejercicio 3
    if numero_random % 2 == 0 and numero_random < 15000:
        numero_par_menor += 1

porcentaje = (numero_par_menor * 100) // 20000

print(
    "Multiplo de 7: ",
    multiplos_7,
    "Multiplo de 5: ",
    multiplos_5,
    "Multiplo de 9: ",
    multiplos_9,
)
print("Numero mayor: ", numero_mayor)
print("Numero par menor a 15000:", numero_par_menor)
print("Porcentaje: ", trunc(porcentaje))
