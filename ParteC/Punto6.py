import cv2
import numpy as np
import matplotlib.pyplot as plt

def obtener_contornos(image_path):

    # Cargar la imagen
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Aplicar un umbral para binarizar la imagen
    _, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    
    # Encontrar los contornos
    contornos, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return contornos

def dibujar_contornos(contornos):

    for contorno in contornos:
        for punto in contorno:
            x, y = punto[0]
            plt.scatter(x, y, c='r', s=2)
    
    plt.gca().invert_yaxis()  # Invertir el eje Y para que coincida con la representación de imagen
    plt.title('Coordenadas de los Contornos')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def main():
    # Ruta de la imagen del logotipo
    image_path = 'ruta_a_la_imagen_del_logo.png'
    
    # Obtener los contornos
    contornos = obtener_contornos(image_path)
    
    # Dibujar los contornos
    dibujar_contornos(contornos)

    # Imprimir las coordenadas X e Y de los contornos
    for i, contorno in enumerate(contornos):
        print(f"Contorno {i + 1}:")
        for punto in contorno:
            x, y = punto[0]
            print(f"({x}, {y})")

# Ejecutar la función principal
if __name__ == "__main__":
    main()