import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def tipo_sistema(omega_n, zeta):

    if zeta < 1:
        return "Subamortiguado"
    elif zeta == 1:
        return "Críticamente Amortiguado"
    else:
        return "Sobreamortiguado"

def graficar_respuesta(num, den):

    sistema = signal.TransferFunction(num, den)
    t, y = signal.step(sistema)

    plt.figure(figsize=(10, 6))
    plt.plot(t, y)
    plt.title('Respuesta Temporal del Sistema')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Respuesta')
    plt.grid(True)
    plt.show()

def main():
    print("Ingrese los coeficientes de la función de transferencia de segundo orden.")
    
    # Coeficientes de la función de transferencia
    a2 = float(input("Coeficiente a2 (de s^2): "))
    a1 = float(input("Coeficiente a1 (de s): "))
    a0 = float(input("Coeficiente a0 (constante): "))
    
    # Numerador y denominador de la función de transferencia
    num = [1]  # Numerador para un sistema estándar de segundo orden
    den = [a2, a1, a0]
    
    # Parámetros del sistema
    omega_n = np.sqrt(a0)  # Frecuencia natural (omega_n) aproximada
    zeta = a1 / (2 * np.sqrt(a2 * a0))  # Coeficiente de amortiguamiento

    tipo = tipo_sistema(omega_n, zeta)
    print(f"Tipo de sistema: {tipo}")

    # Graficar la respuesta del sistema
    graficar_respuesta(num, den)

# Ejecutar la función principal
if __name__ == "__main__":
    main()