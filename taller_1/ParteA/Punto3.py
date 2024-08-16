import math

x = 3
y = 4
z = 5

def rect_to_cylindrical(x, y, z):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta, z

def rect_to_spherical(x, y, z):
    rho = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z / rho)
    return rho, theta, phi

r, theta, z_cyl = rect_to_cylindrical(x, y, z)
print("Coordenadas cilíndricas:")
print("r:", r)
print("theta:", theta)
print("z:", z_cyl)

rho, theta_sph, phi = rect_to_spherical(x, y, z)
print("Coordenadas esféricas:")
print("rho:", rho)
print("theta:", theta_sph)
print("phi:", phi)