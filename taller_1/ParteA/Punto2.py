import numpy as np

# Inicializar las matrices
matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matriz2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])


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