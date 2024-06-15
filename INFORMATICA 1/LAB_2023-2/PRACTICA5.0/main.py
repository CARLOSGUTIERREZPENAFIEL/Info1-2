from utilidades import*
print("MENU")
print("1. usuario registrado")
print("2. usuario visitante")
print("3. salir del sistema")

opcion = (input("seleccionar una opcion: \n"))
caracteres_validos = "123"
while opcion not in caracteres_validos:
    opcion = (input("ingrese un caracter correcto: \n"))

if opcion == "1":
    registrado()
elif opcion == "2":
    visitante()
elif opcion =="3":
    print("")
    