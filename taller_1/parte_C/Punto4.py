import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def dibujar_vector(x, y, z):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    origen = [0, 0, 0]

    ax.quiver(
        origen[0], origen[1], origen[2], x, y, z, color="b", arrow_length_ratio=0.1
    )

    ax.set_xlim([0, max(0, x) + 1])
    ax.set_ylim([0, max(0, y) + 1])
    ax.set_zlim([0, max(0, z) + 1])

    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")
    ax.set_title("Sistema de Coordenadas 3D")
    plt.show()


def main():
    print("Ingrese las coordenadas del vector en 3D.")

    x = float(input("Coordenada X: "))
    y = float(input("Coordenada Y: "))
    z = float(input("Coordenada Z: "))

    dibujar_vector(x, y, z)


if __name__ == "__main__":
    main()
