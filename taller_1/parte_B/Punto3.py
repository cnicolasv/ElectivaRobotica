import math


def volumen_prisma(l, w, h):

    return l * w * h


def volumen_piramide(l, w, h):

    area_base = l * w
    return (1 / 3) * area_base * h


def volumen_cono_truncado(R, r, h):
    """
    Parámetros:
    R (float): Radio de la base mayor.
    r (float): Radio de la base menor.
    h (float): Altura del cono truncado.

    """
    return (1 / 3) * math.pi * h * (R**2 + R * r + r**2)


def volumen_cilindro(r, h):

    return math.pi * r**2 * h


def main():
    print("Seleccione el sólido para calcular el volumen:")
    print("1. Prisma Rectangular")
    print("2. Pirámide Rectangular")
    print("3. Cono Truncado")
    print("4. Cilindro")

    opcion = int(input("Ingrese el número de la opción seleccionada: "))

    if opcion == 1:
        l = float(input("Ingrese la longitud de la base (l): "))
        w = float(input("Ingrese el ancho de la base (w): "))
        h = float(input("Ingrese la altura (h): "))
        v = volumen_prisma(l, w, h)
        print(f"El volumen del prisma rectangular es: {v:.2f} unidades cúbicas")

    elif opcion == 2:
        l = float(input("Ingrese la longitud de la base (l): "))
        w = float(input("Ingrese el ancho de la base (w): "))
        h = float(input("Ingrese la altura (h): "))
        v = volumen_piramide(l, w, h)
        print(f"El volumen de la pirámide rectangular es: {v:.2f} unidades cúbicas")

    elif opcion == 3:
        R = float(input("Ingrese el radio de la base mayor (R): "))
        r = float(input("Ingrese el radio de la base menor (r): "))
        h = float(input("Ingrese la altura (h): "))
        v = volumen_cono_truncado(R, r, h)
        print(f"El volumen del cono truncado es: {v:.2f} unidades cúbicas")

    elif opcion == 4:
        r = float(input("Ingrese el radio de la base (r): "))
        h = float(input("Ingrese la altura (h): "))
        v = volumen_cilindro(r, h)
        print(f"El volumen del cilindro es: {v:.2f} unidades cúbicas")

    else:
        print("Opción no válida. Seleccione una opción entre 1 y 4.")


if __name__ == "__main__":
    main()
