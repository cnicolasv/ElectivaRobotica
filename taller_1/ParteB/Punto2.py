import random

def generar_numeros_aleatorios(cantidad, minimo, maximo):

    return [random.randint(minimo, maximo) for _ in range(cantidad)]

def main():
    # Solicitar al usuario la cantidad de números a generar
    cantidad = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    
    # Solicitar al usuario el rango mínimo y máximo
    minimo = int(input("Ingrese el valor mínimo del rango: "))
    maximo = int(input("Ingrese el valor máximo del rango: "))
    
    # Validar que el valor máximo sea mayor que el valor mínimo
    if minimo > maximo:
        print("El valor máximo debe ser mayor o igual al valor mínimo.")
        return
    
    # Generar números aleatorios
    numeros_aleatorios = generar_numeros_aleatorios(cantidad, minimo, maximo)
    
    # Mostrar los números aleatorios
    print(f"Números generados: {numeros_aleatorios}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()