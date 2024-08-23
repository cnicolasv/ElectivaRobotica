import random

def generar_numeros_aleatorios(cantidad, minimo, maximo):

    return [random.randint(minimo, maximo) for _ in range(cantidad)]

def main():
    
    cantidad = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    
    minimo = int(input("Ingrese el valor mínimo del rango: "))
    maximo = int(input("Ingrese el valor máximo del rango: "))
    
    if minimo > maximo:
        print("El valor máximo debe ser mayor o igual al valor mínimo.")
        return

    numeros_aleatorios = generar_numeros_aleatorios(cantidad, minimo, maximo)
    
    print(f"Números generados: {numeros_aleatorios}")

if __name__ == "__main__":
    main()