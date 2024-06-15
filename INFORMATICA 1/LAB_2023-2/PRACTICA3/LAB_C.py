
r = float(input("ingresar el valor del radio: "))

h = float(input("ingresar valor de la altura: "))

area = (2*3.1416*r*h) + 2*3.1416*(r**2)

volumen = (3.1416*r**2*h)
print("la cantidad de material necesario para cubri la caneca es: " ,area)
print("la cantidad de liquido capaz de almacenar es: ",volumen)