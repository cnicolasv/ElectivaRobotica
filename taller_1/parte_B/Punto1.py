def calcular_potencia(voltage, corriente):

    return voltage * corriente


def main():
    voltage = float(input("Ingrese el valor del voltaje (V): "))
    corriente = float(input("Ingrese el valor de la corriente (A): "))

    potencia = calcular_potencia(voltage, corriente)

    print(f"La potencia consumida por el circuito es: {potencia:.2f} W")


if __name__ == "__main__":
    main()
