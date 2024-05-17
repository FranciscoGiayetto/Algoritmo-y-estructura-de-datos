import random
from math import trunc

random.seed(123456)

multiplos_4=0
multiplos_6=0
multiplos_4_6=0
numero_menor=10 ** 30
numero_promedio=0
suma_promedio=0
promedio_menores_20=0
suma_8=0

for i in range(30000):
    numero_random=random.randint(1, 50000)

    if numero_random % 4 == 0:
        multiplos_4 += 1
    if numero_random % 6 == 0:
        multiplos_6 += 1
    if numero_random % 4 == 0 and numero_random % 6 == 0:
        multiplos_4_6 += 1
    
    if numero_random % 10 in (2,4,6):
        if numero_menor > numero_random:
            numero_menor = numero_random
    
    if numero_random % 2 != 0 and numero_random > 25000:
        suma_promedio += numero_random
        numero_promedio += 1
    
    if numero_random > 20000:
        promedio_menores_20 += 1
    
    if numero_random % 8 == 0 and numero_random % 12 !=0:
        suma_8 += numero_random


promedio= trunc(suma_promedio // numero_promedio)
promedio_numeros_menores_20= (promedio_menores_20 * 100) //30000


print(f'Ejercicio 1: multiplos de 4: {multiplos_4}, multiplos 6: {multiplos_6}, multiplos 4 y 6: {multiplos_4_6}')
print(f'Ejercicio 2: menor numero: {numero_menor}')
print(f'Ejercicio 3: promedio de numeros mayores a 25000: {promedio}')
print(f'Ejercicio 4: promedio de numeros mayores a 20000 y menores a 25000: {promedio_numeros_menores_20}')
print(f'Ejercicio 5: suma de numeros divisibles por 8: {suma_8}')

