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
    plt.title("Respuesta Temporal del Sistema")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Respuesta")
    plt.grid(True)
    plt.show()


def main():
    print("Ingrese los coeficientes de la función de transferencia de segundo orden.")

    a2 = float(input("Coeficiente a2 (de s^2): "))
    a1 = float(input("Coeficiente a1 (de s): "))
    a0 = float(input("Coeficiente a0 (constante): "))

    num = [1]
    den = [a2, a1, a0]

    omega_n = np.sqrt(a0)
    zeta = a1 / (2 * np.sqrt(a2 * a0))

    tipo = tipo_sistema(omega_n, zeta)
    print(f"Tipo de sistema: {tipo}")

    graficar_respuesta(num, den)


if __name__ == "__main__":
    main()
