import numpy as np
import matplotlib.pyplot as plt


def calcular_carga_descarga(V0, R, C, tiempo, modo):

    # Parámetros:
    # V0 (float): Voltaje inicial (Voltios).
    # R (float): Resistencia (Ohmios).
    # C (float): Capacitancia (Faradios).
    # tiempo (array): Array de tiempos en segundos.
    # modo (str): 'carga' para la carga, 'descarga' para la descarga.

    tau = R * C  # Constante de tiempo
    if modo == "carga":
        return V0 * (1 - np.exp(-tiempo / tau))
    elif modo == "descarga":
        return V0 * np.exp(-tiempo / tau)
    else:
        raise ValueError("Modo debe ser 'carga' o 'descarga'.")


def main():

    V0 = float(input("Ingrese el valor del voltaje (V): "))
    C_microfaradios = float(input("Ingrese la capacitancia (μF): "))
    R = float(input("Ingrese la resistencia (Ω): "))

    C = C_microfaradios * 1e-6

    # Crear el vector de tiempo
    tiempo = np.linspace(
        0, 5 * (R * C), 1000
    )  # 5 constantes de tiempo para buena visualización

    # Calcular voltajes
    voltaje_carga = calcular_carga_descarga(V0, R, C, tiempo, "carga")
    voltaje_descarga = calcular_carga_descarga(V0, R, C, tiempo, "descarga")

    plt.figure(figsize=(8, 5))
    plt.plot(tiempo, voltaje_carga, label="Carga del Capacitor")
    plt.plot(tiempo, voltaje_descarga, label="Descarga del Capacitor", linestyle="--")
    plt.title("Carga y Descarga del Capacitor en un Circuito RC")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Voltaje (V)")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
