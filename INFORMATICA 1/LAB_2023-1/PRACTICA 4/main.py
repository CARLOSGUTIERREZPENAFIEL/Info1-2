

from ahorcado import *

print("juego del ahorcado, consiste en descubrir una palabra ya sea seleccionada aleatoriamente o escrita por otro jugador")

# Despliegue de la entrada
printIntro('intro.txt')


letrasIntentadas=''
numeroIntentos = 8
otraVez = 'y'

while otraVez == 'y':
    print(" ** SELECCIONAR MODO DE JUEGO **")
    print("1. ingresar palabra secreta ")
    print("2. seleccionar de un archivo ")
    juego = 1
    while juego == 1:
        mjuego = input("seleccione una opcion : ")
        if mjuego == "1":
            palabra = inputSecret()
            juego = 2
        elif mjuego == "2":
            palabra = pickWord(loadWords("superHeroes.txt"), ",")
            juego = 2
        else: 
            print("el caracter ingresado no coincide con las opciones, por favor intentalo otra vez ")
    
    letraspuestas = obtenerLetrasDisponibles(letrasIntentadas)
    palabraoculta = obtenerParteAdivinada(palabra, letrasIntentadas)

    
         
    
	
    print("usted tiene " , numeroIntentos, " disponibles")
    print("letras disponibles : ", letraspuestas)
    print("palabra secreta : ", palabraoculta)
    print("--------------------------------------------------------------------------------------------------------------")
    ban = 1
         	
	
    while ban == 1:
        letrasingresadas = input("ingrese una letra : ")
        letrasingresadas = letrasingresadas.lower()
        
        while letrasingresadas not in "abcdefghijklmnñopqrstuvwxyz":
            letrasingresadas = input("caracter invalido, por favor intentalo de nuevo :")
            if len(letrasingresadas) != 1:
                letrasingresadas = input("caracter invalido, por favor intentalo de nuevo :").lower()
            
                
            
        
        while verificarLetraIngresada(letrasingresadas,letrasIntentadas) == True:
            letrasingresadas = input("Esta letra ya la uso , escriba otra ").lower()
            while letrasingresadas not in "abcdefghijklmnñopqrstuvwxyz":
                letrasingresadas = input("caracter invalido, por favor intentalo de nuevo :")
                if len(letrasingresadas) != 1:
                    letrasingresadas = input("caracter invalido, por favor intentalo de nuevo :").lower()
       
        letrasIntentadas += letrasingresadas
        
        letraspuestas = obtenerLetrasDisponibles(letrasIntentadas)
        palabraoculta = obtenerParteAdivinada(palabra, letrasIntentadas)
        
        if letrasingresadas in palabra:
            print("letra acertada")
        else:       
            print("letra fallada")
            numeroIntentos -= 1
        
        print("usted tiene " , numeroIntentos, " disponibles")
        print("letras disponibles : ", letraspuestas)
        print("palabra secreta : ", palabraoculta)
        
        if palabraAdivinada(palabra, letrasIntentadas) == True:
            print("felicitaciones, la palabra secreta es: ", palabra, "has ganado un viaje a cuba")
            ban = 0
        if numeroIntentos == 0:
            print("lo lamento, has perdido, la palabra secreta era : ", palabra)
            ban = 0
        print("---------------------------------------------------------------------------------------------------------")
    otra = 1
    while otra == 1:
        otraVez = input("desea jugar otra vez? (y/n):").lower()
        if otraVez == "n":
                otra = 0
             
        elif otraVez == "y":
            letrasIntentadas=''
            numeroIntentos = 8
            otra = 0
        else:
                print("solo puede ingresar las letras y / n")
    
    
        
   
   



