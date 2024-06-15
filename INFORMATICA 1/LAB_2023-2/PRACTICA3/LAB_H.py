devuelta = int(input("ingresar el valor a devolver, debe ser un numero entero mayor a 0, de lo contrario daña el codigo gonorrea: \n"))
while True:
    if devuelta <0:
         devuelta = int(input("ingresar un valor valido: \n"))       
    else:
        break
d1000 = devuelta//1000
aux = devuelta%1000
d500 = aux//500
aux =aux % 500
d200 = aux//200
aux= aux%200
d100= aux//100
aux= aux%100
d50 = aux//50
aux= aux%50
print(f"El valor a devolver es de: \n {d1000} monedas de 1000 \n {d500} mondeas de 500 \n {d200} monedas de 200 \n {d100} monedas de 100 \n {d50} monedas de 50 \n y el resto es de : {aux}")