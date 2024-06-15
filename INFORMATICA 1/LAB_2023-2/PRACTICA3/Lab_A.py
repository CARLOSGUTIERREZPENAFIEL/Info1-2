lado = float(input("ingrese la longitud de los lados iguales, debe ser un numero: \n"))
base = float(input("ingrese la longitud de la base, debe ser un numero: \n"))
while True:
    if lado < base:
        lado = float(input("el valor de los lados iguales debe ser mayor a la base: \n"))
        base = float(input("el valor de la base debe ser menor al de los lados iguales: \n"))
    else:
        break
perimetro = round((2*lado)+ base, 1)
altura = round((lado**2 - (base**2)/4)**(1/2), 1)
area = round((base*altura)/2, 1)
print(f"el perimetro es: {perimetro} \n la altura es :{altura} \n el area es: {area}")