import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dibujar_vector(x, y, z):
    """
    Dibuja un vector en un sistema de coordenadas tridimensional.
    
    Parámetros:
    x (float): Coordenada en el eje X.
    y (float): Coordenada en el eje Y.
    z (float): Coordenada en el eje Z.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Origen del vector
    origen = [0, 0, 0]

    # Dibuja el vector
    ax.quiver(origen[0], origen[1], origen[2], x, y, z, color='b', arrow_length_ratio=0.1)

    # Establece los límites de los ejes
    ax.set_xlim([0, max(0, x) + 1])
    ax.set_ylim([0, max(0, y) + 1])
    ax.set_zlim([0, max(0, z) + 1])

    # Etiquetas de los ejes
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    # Título del gráfico
    ax.set_title('Vector en el Sistema de Coordenadas 3D')

    # Muestra la gráfica
    plt.show()

def main():
    print("Ingrese las coordenadas del vector en 3D.")
    
    # Ingreso de las coordenadas del vector por parte del usuario
    x = float(input("Coordenada X: "))
    y = float(input("Coordenada Y: "))
    z = float(input("Coordenada Z: "))

    # Dibuja el vector
    dibujar_vector(x, y, z)

# Ejecutar la función principal
if __name__ == "__main__":
    main()