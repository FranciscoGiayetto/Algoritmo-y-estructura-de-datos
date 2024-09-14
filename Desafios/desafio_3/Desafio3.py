import soporte
from collections import Counter
def mostrar(lista,numero):
    print('-'*20)
    print(f'Parte {numero}')
    print('-'*20)
    numeros_unicos = list(set(lista))
    print('Numeros unicos ', len(numeros_unicos))

    contador = Counter(lista)
    max_frecuencia = max(contador.values())

    numeros_mas_frecuentes = [num for num, count in contador.items() if count == max_frecuencia]

    print(f"Los números que más se repiten son {numeros_mas_frecuentes} y se repiten {max_frecuencia} veces.")

mostrar(soporte.vector_unknown_range(300000),1)
mostrar(soporte.vector_known_range(300000),2)
