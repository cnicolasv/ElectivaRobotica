import numpy as np

def rotacion_x(angulo):

    matriz = np.array([
        [1, 0, 0],
        [0, np.cos(angulo), -np.sin(angulo)],
        [0, np.sin(angulo), np.cos(angulo)]
    ])
    return matriz

def rotacion_y(angulo):

    matriz = np.array([
        [np.cos(angulo), 0, np.sin(angulo)],
        [0, 1, 0],
        [-np.sin(angulo), 0, np.cos(angulo)]
    ])
    return matriz

def rotacion_z(angulo):

    matriz = np.array([
        [np.cos(angulo), -np.sin(angulo), 0],
        [np.sin(angulo), np.cos(angulo), 0],
        [0, 0, 1]
    ])
    return matriz

# Ejemplo
angulo = np.radians(45)

matriz_x = rotacion_x(angulo)
print("Matriz de rotación en torno al eje X:\n", matriz_x)

matriz_y = rotacion_y(angulo)
print("Matriz de rotación en torno al eje Y:\n", matriz_y)

matriz_z = rotacion_z(angulo)
print("Matriz de rotación en torno al eje Z:\n", matriz_z)