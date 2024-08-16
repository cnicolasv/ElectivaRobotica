import matplotlib.pyplot as plt

def dibujar_letra_ejes(ax, letra, coordenadas):
    """
    Parámetros:
    ax (Axes): Objeto de ejes de matplotlib donde se dibujará la letra.
    letra (str): La letra a dibujar.
    coordenadas (tuple): Coordenadas base (x, y) donde se dibujará la letra.
    """
    x_base, y_base = coordenadas
    
    if letra == 'A':
        # Dibujar la letra 'A' usando líneas
        ax.plot([x_base, x_base + 1], [y_base, y_base + 2], color='blue')  # Línea izquierda
        ax.plot([x_base + 1, x_base + 2], [y_base + 2, y_base], color='blue')  # Línea derecha
        ax.plot([x_base + 0.5, x_base + 1.5], [y_base + 1, y_base + 1], color='blue')  # Línea media
    
    # Puedes añadir más letras aquí con coordenadas y formas personalizadas
    # Añade una condición por cada letra del nombre

def dibujar_nombre():
    fig, ax = plt.subplots()

    # Ejemplo de cómo podrías dibujar un nombre (por ejemplo, "ANA")
    nombre = "ANA"
    base_x = 0
    base_y = 0
    espaciado = 2

    for i, letra in enumerate(nombre):
        dibujar_letra_ejes(ax, letra, (base_x + i * espaciado, base_y))

    # Configuración de los ejes
    ax.set_aspect('equal')
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 5)
    ax.axis('off')  # Opcional: oculta los ejes

    plt.show()

# Ejecutar la función principal
if __name__ == "__main__":
    dibujar_nombre()