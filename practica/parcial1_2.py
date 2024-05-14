import random
from math import trunc
from statistics  import mean
random.seed(20220512)

multiplo_3=0
multiplo_5=0
multiplo_otro=0
numero_mayor= 0
total_promedio=0
contador_pares_multiplos_11=0
lista=[]
for i in range(25000):
    #numero aleatorios
    numero_aleatorio=random.randint(1, 45000)

    #Ejercicio 1
    if numero_aleatorio % 3 == 0:
        multiplo_3 += 1
    elif numero_aleatorio % 5 == 0:
        multiplo_5 += 1
    else:
        multiplo_otro += 1

    #Ejercicio 2
    prueba=str(numero_aleatorio) 
    if prueba[0]== '1':
        if numero_aleatorio > numero_mayor:
            numero_mayor= numero_aleatorio

    #Ejercicio 3
    if numero_aleatorio % 2 == 0 and numero_aleatorio % 11 == 0:
        lista.append(numero_aleatorio)
        total_promedio += numero_aleatorio
        contador_pares_multiplos_11 += 1

print(total_promedio)
print(contador_pares_multiplos_11)
print(mean(lista))
print('Promedio: ', trunc(total_promedio//contador_pares_multiplos_11))
'''print(f'Multiplo de 3: {multiplo_3} multiplo de 5: {multiplo_5} multiplo de ninguno de los dos: {multiplo_otro}')
print('Numero maroy: ', numero_mayor)
print('Promedio: ', trunc(total_promedio//25000))

porcentaje_3= (multiplo_3*100) // 25000
porcentaje_5= (multiplo_5*100) // 25000
porcentaje_otro= (multiplo_otro*100) // 25000

print(f'Porcentajes:  de 3: {porcentaje_3}  de 5: {porcentaje_5}  de ninguno de los dos: {porcentaje_otro}')'''