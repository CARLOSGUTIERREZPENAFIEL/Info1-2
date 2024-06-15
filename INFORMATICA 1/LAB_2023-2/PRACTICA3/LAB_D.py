horas = int(input("ingresa las horas de uso, debe ser un numero entero: \n"))
minutos = int(input("ingrese los minutos de uso, debe ser un numero entero: \n"))
cobro= 0
if minutos > 60:
    aux = minutos//60
    aux1 = minutos%60
    print("su tiempo de uso fueron: " , aux+horas, "horas y ", aux1, "minutos")
tiempo = (horas*60)+minutos
if tiempo >100:
    if tiempo > 1440:
        cobro = (1340* 57)+96000+700
        print("el valor a pagar es de: ", cobro)
    else:
        cobro= ((tiempo-100)* 57)+700
        print("el valor a pagar es de: ", cobro)
else:
    cobro = tiempo*7
    print("el valor a pagar es de: ", cobro)