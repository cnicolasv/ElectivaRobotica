import numpy as np
import matplotlib.pyplot as plt

def resistencia_pt100(temperatura):
    
    R0 = 100  # Resistencia a 0°C
    alpha = 0.00385  # Coeficiente de temperatura
    return R0 * (1 + alpha * temperatura)

def graficar_resistencia_pt100():

    temperaturas = np.linspace(-200, 200, 400)  # Rango de temperaturas
    resistencias = resistencia_pt100(temperaturas)
    
    plt.figure(figsize=(10, 6))
    plt.plot(temperaturas, resistencias, label='Sensor PT100')
    plt.title('Comportamiento del Sensor PT100')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Resistencia (Ohmios)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Ejecutar la función para graficar
if __name__ == "__main__":
    graficar_resistencia_pt100()