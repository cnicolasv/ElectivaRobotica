def resistance_pt100(temperature):
    R0 = 100  # Resistencia a 0°C para PT100
    alpha = 0.00385  # Coeficiente de temperatura para PT100

    if temperature >= 0:
        # Fórmula para temperaturas >= 0°C
        resistance = R0 * (1 + alpha * temperature)
    else:
        # Fórmula para temperaturas < 0°C (más precisa)
        A = 3.9083e-3
        B = -5.775e-7
        C = -4.183e-12  # Utilizado solo para temperaturas < -200°C
        resistance = R0 * (1 + A * temperature + B * temperature * 2)

    return resistance


# Ejemplo
temperatura = 50  # Temperatura en °C
resistencia = resistance_pt100(temperatura)
print(f"La resistencia del PT100 a {temperatura}°C es {resistencia:.2f} ohmios")
