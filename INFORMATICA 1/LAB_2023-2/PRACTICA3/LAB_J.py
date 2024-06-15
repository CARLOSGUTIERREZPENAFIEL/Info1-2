numero1 = float(input("ingrese el primer numero entero , de lo contrario el programa no funcinara: "))
numero2= float(input("ingrese el segundo numero entero , de lo contrario el programa no funcinara: "))
mcd = 1
div = 2
while True:
    if numero1%1 != 0 or numero1<= 0 :
        numero1 = float(input("primer numero invalido, ingrese uno nuevo: \n"))
    elif  numero2 %1 != 0 or numero2<= 0:
        numero2 = float(input("segundo numero invaido, ingrese uno nuevo: \n"))
    else:
        break
num1 = int(numero1)
num2 = int(numero2)
while div <= num1 and div <= num2:
    if num1% div == 0 and num2 % div == 0:
        mcd = mcd*div
        num1= num1//div
        num2 = num2//div
    else:
        div += 1
print("El MCD es: ", mcd)