numero = float(input("ingrese un numero entero impar, de lo contrario el programa no funcinara: "))
contador = 0
espacio= "    "
aux = "+"
imagen = ""
while True:
    if numero%1 != 0 or numero%2 == 0:
        numero = float(input("ingrese un numero entero impar valido: \n"))
    else:
        break
longitud = int(numero)
for i in range(longitud,0,-2):
    imagen = (aux*i)+(espacio*contador)+(aux*i)
    contador += 1
    print(imagen)
    imagen = ""