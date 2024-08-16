def calcular_potencia(voltage, corriente):
 
    return voltage * corriente

def main():
    # Solicitar al usuario que ingrese los valores de corriente y voltaje
    voltage = float(input("Ingrese el valor del voltaje (V): "))
    corriente = float(input("Ingrese el valor de la corriente (A): "))

    # Calcular la potencia
    potencia = calcular_potencia(voltage, corriente)

    # Mostrar el resultado
    print(f"La potencia consumida por el circuito es: {potencia:.2f} W")

# Ejecutar la función principal
if __name__ == "__main__":
    main()