import cv2
import numpy as np
import matplotlib.pyplot as plt


def reducir_resolucion(img, escala):
    ancho = int(img.shape[1] * escala)
    alto = int(img.shape[0] * escala)
    return cv2.resize(img, (ancho, alto), interpolation=cv2.INTER_AREA)


def obtener_contornos(image_path):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = reducir_resolucion(img, 0.4)

    _, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    contornos, _ = cv2.findContours(img_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    return img, contornos


def dibujar_contornos(ax, img, contornos, color, tamaño_punto):

    for contorno in contornos:
        for punto in contorno:
            x, y = punto[0]
            ax.scatter(x, y, c=color, s=tamaño_punto)

    ax.invert_yaxis()
    ax.set_title("Contornos")
    ax.axis("off")


def main():

    imagen1 = "Ferrari.jpg"
    imagen2 = "Lambo.jpg"

    img1, contornos1 = obtener_contornos(imagen1)
    img2, contornos2 = obtener_contornos(imagen2)

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    dibujar_contornos(axs[0], img1, contornos1, color="b", tamaño_punto=1)
    dibujar_contornos(axs[1], img2, contornos2, color="r", tamaño_punto=1)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
