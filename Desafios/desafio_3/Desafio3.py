import soporte
from collections import Counter

#Parte 1
print('-'*20)
print('Parte 1')
print('-'*20)
lista = soporte.vector_unknown_range(300000)
numeros_unicos = list(set(lista))
print('Numeros unicos ', len(numeros_unicos))


contador = Counter(lista)
max_frecuencia = max(contador.values())  # La mayor cantidad de repeticiones

numeros_mas_frecuentes = [num for num, count in contador.items() if count == max_frecuencia]

print(f"Los números que más se repiten son {numeros_mas_frecuentes} y se repiten {max_frecuencia} veces.")

#Parte 2
print('-'*20)
print('Parte 2')
print('-'*20)
lista = soporte.vector_known_range(300000)
numeros_unicos = list(set(lista))
print('Numeros unicos ', len(numeros_unicos))


contador = Counter(lista)
max_frecuencia = max(contador.values())  # La mayor cantidad de repeticiones

numeros_mas_frecuentes = [num for num, count in contador.items() if count == max_frecuencia]

print(f"Los números que más se repiten son {numeros_mas_frecuentes} y se repiten {max_frecuencia} veces.")