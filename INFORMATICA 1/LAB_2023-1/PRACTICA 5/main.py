
from utilidades import *

print("MENU")
print("1. usuario registrado")
#print("2. usuario visitante")
print("2. salir del sistema")

opcion = (input("seleccionar una opcion: "))
caracteres_validos = "123"
while not opcion in caracteres_validos:
    opcion = (input("ingrese un caracter correcto: "))

if opcion == "1":
    registrado()
#elif opcion == "2":
    #visitante()
elif opcion =="2":
    print("")
    
                
            
                 
             
            
         