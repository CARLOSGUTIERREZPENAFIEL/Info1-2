numero = float(input("ingrese un numero entero impar, de lo contrario el programa no funcinara: "))
contador = 0
aux = "*"
while True:
    if numero%1 != 0 or numero%2 == 0:
        numero = float(input("ingrese un numero entero impar valido: \n"))
    else:
        break
longitud = int(numero)
for i in range(1,longitud +1, 2):
    print(aux*i)
for j in range(longitud-2, 0,-2):
    print(aux*j)
    