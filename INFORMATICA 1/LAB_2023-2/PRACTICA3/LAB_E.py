kilometros= float(input("Ingrese los kilometros, debe ser un numero : \n "))
while True:
    if kilometros < 0:
        kilometros= float(input("Ingrese u numero de kilometros valido: \n"))
    else : 
        break
cambio= int((kilometros//5678))
print("El carro ha tenido " , cambio , " cambios de aceite")

