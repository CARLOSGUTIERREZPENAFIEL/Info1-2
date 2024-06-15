num = float(input("ingrese un numero entero, si no es un entero el programa no funcionara: \n"))
while True:
    if num//1 != num:
        num = float(input("ingrese un numero entero valido: \n"))
    break
if num%2 == 0:
    print("Es un numero par")
else: 
    print("Es un numero impar")