import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def dibujar_letra_ejes(ax, letra, coordenadas):

    x_base, y_base = coordenadas

    if letra == "A":
        ax.plot(
            [x_base, x_base + 0.75], [y_base, y_base + 2], color="blue"
        )  # Línea izquierda
        ax.plot(
            [x_base + 0.75, x_base + 1.5], [y_base + 2, y_base], color="blue"
        )  # Línea derecha
        ax.plot(
            [x_base + 0.4, x_base + 1.1], [y_base + 1, y_base + 1], color="blue"
        )  # Línea media

    elif letra == "D":
        ax.plot(
            [x_base + 0.5, x_base + 0.5], [y_base, y_base + 2], color="blue"
        )  # Línea izquierda
        # Arco de la "D"
        arc = patches.Arc(
            [x_base + 0.7, y_base + 1],
            width=1.5,
            height=2,
            angle=0,
            theta1=260,
            theta2=100,
            color="blue",
            linewidth=1.5,
        )
        ax.add_patch(arc)

    elif letra == "V":
        ax.plot(
            [x_base, x_base + 0.75], [y_base + 2, y_base], color="blue"
        )  # Línea izquierda
        ax.plot(
            [x_base + 0.75, x_base + 1.5], [y_base, y_base + 2], color="blue"
        )  # Línea derecha

    elif letra == "I":
        ax.plot(
            [x_base + 0.5, x_base + 1.5], [y_base + 2, y_base + 2], color="blue"
        )  # Línea superior
        ax.plot(
            [x_base + 1, x_base + 1], [y_base, y_base + 2], color="blue"
        )  # Línea vertical
        ax.plot(
            [x_base + 0.5, x_base + 1.5], [y_base, y_base], color="blue"
        )  # Línea inferior

    elif letra == "L":
        ax.plot(
            [x_base + 0.5, x_base + 0.5], [y_base, y_base + 2], color="blue"
        )  # Línea vertical
        ax.plot(
            [x_base + 0.5, x_base + 1.5], [y_base, y_base], color="blue"
        )  # Línea horizontal inferior

    elif letra == "C":
        arc = patches.Arc(
            [x_base + 1, y_base + 1],
            width=1.5,
            height=2,
            angle=0,
            theta1=55,
            theta2=310,
            color="blue",
            linewidth=1.5,
        )
        ax.add_patch(arc)

    elif letra == "M":
        ax.plot([x_base, x_base], [y_base, y_base + 2], color="blue")  # Línea izquierda
        ax.plot(
            [x_base, x_base + 0.75], [y_base + 2, y_base + 1], color="blue"
        )  # Diagonal izquierda
        ax.plot(
            [x_base + 0.75, x_base + 1.5], [y_base + 1, y_base + 2], color="blue"
        )  # Diagonal derecha
        ax.plot(
            [x_base + 1.5, x_base + 1.5], [y_base + 2, y_base], color="blue"
        )  # Línea derecha

    elif letra == "U":
        ax.plot(
            [x_base, x_base], [y_base + 0.75, y_base + 2], color="blue"
        )  # Línea izquierda
        ax.plot(
            [x_base + 1, x_base + 1], [y_base + 0.75, y_base + 2], color="blue"
        )  # Línea derecha
        arc = patches.Arc(
            [x_base + 0.5, y_base + 0.75],
            width=1,
            height=1.5,
            angle=0,
            theta1=180,
            theta2=360,
            color="blue",
            linewidth=1.5,
        )
        ax.add_patch(arc)

    elif letra == "R":
        ax.plot([x_base, x_base], [y_base, y_base + 2], color="blue")  # Línea izquierda
        arc = patches.Arc(
            [x_base, y_base + 1.5],
            width=2,
            height=1,
            angle=0,
            theta1=270,
            theta2=90,
            color="blue",
            linewidth=1.5,
        )
        ax.add_patch(arc)  # Arco superior
        ax.plot(
            [x_base, x_base + 1], [y_base + 1, y_base], color="blue"
        )  # Línea diagonal inferior

    elif letra == "O":
        arc = patches.Arc(
            [x_base + 1, y_base + 1],
            width=1.5,
            height=2,
            angle=0,
            theta1=0,
            theta2=360,
            color="blue",
            linewidth=1.5,
        )
        ax.add_patch(arc)

    elif letra == "N":
        ax.plot(
            [x_base + 0.25, x_base + 0.25], [y_base, y_base + 2], color="blue"
        )  # Línea izquierda
        ax.plot(
            [x_base + 0.25, x_base + 1.5], [y_base + 2, y_base], color="blue"
        )  # Diagonal
        ax.plot(
            [x_base + 1.5, x_base + 1.5], [y_base, y_base + 2], color="blue"
        )  # Línea derecha

    elif letra == "S":
        arc = patches.Arc(
            [x_base + 0.7, y_base + 1.5],
            width=1.2,
            height=1,
            angle=0,
            theta1=40,
            theta2=270,
            color="blue",
            linewidth=1.5,
        )
        ax.add_patch(arc)
        arc = patches.Arc(
            [x_base + 0.7, y_base + 0.5],
            width=1.2,
            height=1,
            angle=0,
            theta1=210,
            theta2=90,
            color="blue",
            linewidth=1.5,
        )
        ax.add_patch(arc)


def dibujar_nombres(nombres):
    fig, ax = plt.subplots()

    base_x = 0
    base_y = 0
    espaciado = 2
    salto_linea = 3.5  # Espacio vertical entre las líneas de texto

    for posicion, nombre in enumerate(nombres):
        y = (
            base_y + posicion * salto_linea
        )  # Calcula la posición vertical para cada nombre
        for i, letra in enumerate(nombre):
            dibujar_letra_ejes(ax, letra, (base_x + i * espaciado, y))

    # Configuración de los ejes
    ax.set_aspect("equal")
    ax.set_xlim(-1, 14)
    ax.set_ylim(-1, 14)
    ax.axis("off")
    plt.show()


if __name__ == "__main__":
    nombres = ["DAVID", "LAURA", "CAMILO", "NICOLAS"]
    dibujar_nombres(nombres)
