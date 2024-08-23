def mostrar_info_robot(tipo_robot):

    if tipo_robot == "1":
        print("Robot Cilíndrico")
        print("Número de Articulaciones: 3")
        print("1 Articulación rotacional (base)")
        print("1 Articulación prismática (eje z)")
        print("1 Articulación rotacional (eje x)")

    elif tipo_robot == "2":
        print("Robot Cartesiano")
        print("Número de Articulaciones: 3")
        print("3 Articulaciones prismáticas (movimiento en x, y, z)")

    elif tipo_robot == "3":
        print("Robot Esférico")
        print("Número de Articulaciones: 3")
        print("1 Articulación rotacional (base)")
        print("1 Articulación rotacional (eje z)")
        print("1 Articulación rotacional (alrededor del eje de la herramienta)")

    else:
        print("Opción no válida. Seleccione un número entre 1 y 3.")


def main():
    print("Seleccione el tipo de robot:")
    print("1. Robot Cilíndrico")
    print("2. Robot Cartesiano")
    print("3. Robot Esférico")

    tipo_robot = input("Ingrese el número de la opción seleccionada: ")

    mostrar_info_robot(tipo_robot)


if __name__ == "__main__":
    main()
