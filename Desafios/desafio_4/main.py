import csv
import math

# Clase Point que representa un punto en el plano
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Método para calcular la distancia entre dos puntos usando el teorema de Pitágoras
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

# Función para leer los puntos desde el archivo CSV
def read_points(file_name):
    points = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            x, y = int(row[0]), int(row[1])
            points.append(Point(x, y))
    return points

# Función de fuerza bruta para encontrar las distancias mínima y máxima
def find_min_max_distances(points):
    dmin = math.inf
    dmax = 0
    
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            d = points[i].distance(points[j])
            if d < dmin:
                dmin = d
            if d > dmax:
                dmax = d
    
    return round(dmin), round(dmax)

# Ruta del archivo CSV
file_name = 'puntos.csv'

# Leer los puntos desde el archivo
points = read_points(file_name)

# Encontrar las distancias mínima y máxima
dmin, dmax = find_min_max_distances(points)

# Mostrar los resultados
print(f"Distancia mínima: {dmin}")
print(f"Distancia máxima: {dmax}")
