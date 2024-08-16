import math

def area_circulo(diametro):

    radio = diametro / 2
    return math.pi * (radio * 2)

def fuerza_avance(presion, diametro_piston):

    area_piston = area_circulo(diametro_piston)
    return presion * area_piston

def fuerza_retroceso(presion, diametro_piston, diametro_vastago):

    area_piston = area_circulo(diametro_piston)
    area_vastago = area_circulo(diametro_vastago)
    return presion * (area_piston - area_vastago)

# Ejemplo
presion = 700000  # Presión en pascales
diametro_piston = 0.1  # Diámetro del pistón en metros
diametro_vastago = 0.02  # Diámetro del vástago en metros

fuerza_av = fuerza_avance(presion, diametro_piston)
fuerza_ret = fuerza_retroceso(presion, diametro_piston, diametro_vastago)

print(f"Fuerza de avance: {fuerza_av:.2f} N")
print(f"Fuerza de retroceso: {fuerza_ret:.2f} N")