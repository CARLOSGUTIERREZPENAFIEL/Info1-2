a= int(input("Ingrese el valor de a el cual sea un numero entero: \n"))
b= int(input("Ingrese el valor de b el cual sea un numero entero: \n"))
c= int(input("Ingrese el valor de c el cual sea un numero entero: \n"))
discriminante=((b**2)-4*(a)*(c))
if a==0:
    x1= -(c/b)
    print(x1)
elif discriminante >0:
    x1= (-b+(((b**2)-(4*a*c))**0.5))/(2*a)
    x2= (-b-(((b**2)-(4*a*c))**0.5))/(2*a)
    print (f"Las soluciones de la ecuacion son: {x1} y {x2}")
elif discriminante == 0:
    x12=(b//2*a)
    print(f"La unica solucion de la ecuacion es: {x12}")
else :
    x1= (-b+((-1*(b**2)-4*a*c)**0.5))/(2*a)
    x2= (-b-((-1*(b**2)-4*a*c)**0.5))/(2*a)
    print (f"Las soluciones de la ecuacion son en los imaginarios y son: {x1} y {x2} ")
    
