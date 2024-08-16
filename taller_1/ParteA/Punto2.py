import numpy as np

# Inicializar las matrices
matriz1 = np.array([[6, 3, 3], [4, 9, 8], [7, 0, 1]])

matriz2 = np.array([[7, 7, 4], [9, 2, 3], [5, 6, 4]])


suma = matriz1 + matriz2
print("Suma de las matrices:\n", suma)

resta = matriz1 - matriz2
print("Resta de las matrices:\n", resta)

producto_punto = matriz1 * matriz2
print("Producto punto de las matrices:\n", producto_punto)

producto_cruz = np.dot(matriz1, matriz2)
print("Producto cruz de las matrices:\n", producto_cruz)

division = matriz1 / matriz2
print("División de las matrices (elemento por elemento):\n", division)
