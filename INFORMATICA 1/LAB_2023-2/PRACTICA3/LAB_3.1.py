x = input("ingresar una letra: \n").lower()
con= "bcdfghjklmnpqrstvwxyz"
voc = "aeiou"
while True:
    if len(x)== 1:
        if x in con:
            print("es consonante")
            break
        elif x in voc:
            print("es una vocal")
            break
        else:
            x = ("ingrese una letra valida \n")
    else:
        x = input("ingrese una letra valida \n")
    

        
        

    