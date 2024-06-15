inicio = input("ingrese el tiempo de inicio en formato: HHMMSS con un solo numero entero, de lo contrario el programa no funcionara: \n")
start = int(inicio)
while True:
    if len(inicio)!= 6 or start<0 or start >235959:
        inicio = input("ingrese el tiempo de inicio valido: \n")
        start = int(inicio)
    else:
        break
fin = input("ingrese el tiempo de fin en formato: HHMMSS con un solo numero entero, de lo contrario el programa no funcionara: \n")
end = int(fin)
while True:
    if len(fin)!= 6 or start<0 or end >235959:
        inicio = input("ingrese el tiempo de inicio valido: \n")
        start = int(inicio)
    else:
        break 
horas_I= start//10000
aux= start%10000
min_I= aux//100
seg_I= aux%100
horas_F= end//10000
aux1= end%10000
min_F= aux1//100
seg_F= aux1 %100
seg_F
precio= 0
tiempoI = (horas_I*3600)+(min_I*60)+seg_I
tiempoF = (horas_F*3600)+(min_F*60)+seg_F
if start < end:
    precio= ((tiempoF - tiempoI)*2) + 1000
    print("el costo del servicio de streaming es de: ", precio)
else:
    precio = (((86400-tiempoI)+tiempoF)*2)+1000
    print("el costo del servicio de streaming es de: ", precio)

    
    
    