import numpy as np

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

suma = vector1 + vector2
print("Suma:", suma)

resta = vector1 - vector2
print("Resta:", resta)

producto_punto = np.dot(vector1, vector2)
print("Producto punto:", producto_punto)

producto_cruz = np.cross(vector1, vector2)
print("Producto cruz:", producto_cruz)

division = vector1 / vector2
print("División:", division)
