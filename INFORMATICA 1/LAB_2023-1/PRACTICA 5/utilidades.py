# -*- coding: utf-8 -*-
from datetime import datetime
def validar_contraseña(contraseña):
    num = "1234567890"
    nuevo_num = ""
    if len(contraseña) != 4:
        return False
    for i in range(0, len(contraseña)):
        if contraseña[i] in num:
            nuevo_num += contraseña[i]
        else: 
            return False
    if nuevo_num == contraseña:
        return True
    pass



def validar_nombre(nombre):
    '''
    Valida nombre válido (solo letras y espacios)
    Argumentos:
        nombre: String a validar
    return -> Boolean (True or False) si es valido o no
    '''
    
    abc = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNñÑoOpPqQrRsStTuUvVwWxXyYzZáéíóú "
    nueva = ""
    for i in range(0 , len(nombre)):
        if nombre[i] in abc:
            nueva += nombre[i]
        else:
            return False
            break
    if nueva == nombre:
       return True
        
    
    pass

def validar_documento(documento):
    '''
    Valida un número de documento. Debe contener 10 caracteres, todos numéricos.
    
    Argumentos:
        documento: string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    num = "1234567890"
    nuevo_num = ""
    if len(documento) != 10:
        return False
    for i in range(0, len(documento)):
        if documento[i] in num:
            nuevo_num += documento[i]
        else: 
            return False
    if nuevo_num == documento:
        return True
    pass


def split(string , separador):
    lista = []
    partes = ""
    for i in string:
        if i == separador :
            lista.append(partes)
            partes = ""
        else:
            partes += i
    lista.append(partes)
    return lista

    pass

def mi_pop(lista, posicion):
    a = False
    while not a: 
        if posicion < 0 or posicion >= len(lista):
            #print("posicion fuera del rango")
            try:
                posicion = int(input("Error: caracter invalido, ingresa una nueva posicion : "))
                
            except ValueError:
                print("la posicion debe ser un numero entero")
        else:
            a = True   
    nueva_lista = []
    for i in range(len(lista)):
        if i != posicion:
            nueva_lista.append(lista[i])
    return nueva_lista


def archivos(archivo):
    diccionario_usuarios = {}
    diccionario_estaciones = {}
    diccionario_municipios = {}
    diccionario_registros = {}
    digitos = "0123456789"
    texto = open(archivo, "r")
    for linea in texto:
        if linea != "\n":
            if linea[0] == "<":
                usuario = (split(linea[1:-2], ";"))
                diccionario_usuarios[usuario[0]] = usuario
                
            elif linea[0] == ":":
                diccionario_municipios = split(linea [1:-1], ",")
            elif linea[1] ==  ",":
                estaciones = (split(linea[0:-1], ","))
                diccionario_estaciones[estaciones[0]] = estaciones
                
            elif linea[4] == "-":
                registros = (split(linea[0:-1], ";"))
                diccionario_registros[registros[1]]= registros
                
        
    texto.close()
    datos = {"usuarios": diccionario_usuarios, "municipios": diccionario_municipios, "estaciones": diccionario_estaciones, "registros": diccionario_registros}
    return datos

#print(archivos("registros_.txt"))
def registrado():
    a = False
    contador = 3
    documento = input("ingresar documento: ")
    validar = validar_documento(documento)
    while validar == False:
        
        documento = input("ingresar el documento correctamente: ")
        validar = validar_documento(documento)
    datos = archivos("registros_.txt")
    usuarios = datos["usuarios"]
    while a == False:
        if documento in usuarios:
            a = True
            contraseña = input("ingrese la contraseña: ")
            validar = validar_contraseña(contraseña)
            while validar == False:
                contraseña = input("ingresar una contraseña valida: ")
                validar = validar_contraseña(contraseña)
            while contador > 0:
                if contraseña in usuarios[documento]:
                    usuario = (usuarios[documento])
                    nombre = usuario[1]
                    rol = usuario[3]
                    print("bienvenido" , nombre)
                    print("su rol es: ", rol)
                    
                    if rol == "Operador":
                        print("tu rol es: Operador pero no tengo tu menu")
                        
                        administrador()
                    elif rol == "Administrador":
                        administrador()
                        
                    break
                else:
                    contraseña = input("contraseña no encontrada, ingrese una correcta: ")
                    validar = validar_contraseña(contraseña)
                    contador -= 1
                    print("intentos permitidos: ", contador)
                    while validar == False:
                        contraseña = input("digite una contraseña valida: ")
                        validar = validar_contraseña(contraseña)
        else:
            documento = input("ingrese un documento registrado: ")
            a = False
                    
def menu_inicial():
    limpiar_pantalla()
    print("MENU")
    print("1. usuario registrado")
    print("2. usuario visitante")
    print("3. salir del sistema")
    
    opcion = (input("seleccionar una opcion: "))
    caracteres_validos = "123"
    while not opcion in caracteres_validos:
        opcion = (input("ingrese un caracter correcto: "))
    
    if opcion == "1":
        registrado()
    elif opcion == "2":
        visitante()
    elif opcion =="3":
        print("")
    
             
def operador():
     print("1. seleccionar el municipio de la estacion")
     print("2. seleccionar ")
    
    
    
    
def administrador():
    
    print("1. volver al menu de inicio")
    #print("2. gestionar estaciones")
    print("2. gestionar usuario")
    #print("4. depuracion de registros")
    opcion = input("seleccione una opcion: ")
    
    
    caracteres = "1234"
    while not opcion in caracteres:
        opcion = input("ingrese un caracter valido: ")
    if opcion == "1":
        menu_inicial()
    elif opcion == "2":
        
        gestionar_usuario()
   # elif opcion == "3":
    #    gestionar_usuario()
    #elif opcion == "4":
     #   print("lo siento esta opcion no la habia hecho")
      #  gestionar_usuario()
        
def crear_estacion():        
        
    datos = archivos("registros_.txt")
    estaciones = datos["estaciones"]
    municipios = datos["municipios"]
    aux= []
    esta = []
        
    aux = estaciones.values()  
    for i in aux:
        esta.append(estaciones[i[1]])
    
    print("lista de estaciones")
    for i in range(len(esta)):
        print(f"{i+1}. {esta[i]}")
    
    nueva_estacion = input("ingrese el nombre de la nueva estacion: ")
    
    print(municipios)
    
    print("lista de municipios")
    for i in range(len(municipios)):
        print(f"{i+1}. {municipios[i]}")
    
    numero = int(input("ingrese el numero del municipio: "))
    validos = 1234567890
    while True:
        if numero in validos:
            if numero >0 and numero <= len(municipios[numero-1]):
                nombre_municipio = municipios[numero-1]
                break
            else:
                numero = input("ingrese un numero valido: ")
                
    print(nombre_municipio, nueva_estacion)
        
    

        
def Gestionar_estaciones():
    print("1. crear estacion")
    print("2. editar estacion")
    print("3. eliminar estacion")
    
    opcion = input("seleccionar una opcion: ")
    caracteres = "123"
    while not opcion in caracteres:
        opcion = input("ingresar un caracter valido: ")
    if opcion == "1":
        crear_estacion()
    elif opcion == "2":
        editar_estacion()
    elif opcion == "3":
        eliminar_estacion()
    
def cargar_datos(datos):
    usu_nuevos = ""
    esta_nuevos = ""
    regis_nuevos = ""
    muni_nuevos = ""
    muni = ""
    usuarios = datos["usuarios"]
    estaciones = datos["estaciones"]
    registros = datos["registros"]
    municipios = datos["municipios"]
    
    valores_usu = usuarios.values()
    for posi in valores_usu:
        docu = posi[0]
        nomb = posi[1]
        clave = posi[2]
        traba = posi[3]
        usu = "<"+docu+";"+nomb+";"+clave+";"+traba+">"+"\n"
        usu_nuevos += usu
    for posi in municipios:
        muni += posi+","
    mun_nuevo = ":"+muni+"\n"
    
    valores_estaciones = estaciones.values()
    for posi in valores_estaciones:
        valor = posi[0]
        lugar = posi[1]
        municipio = posi[2]
        esta = valor+","+lugar+","+municipio+"\n"
        esta_nuevos += esta
    parametros = "PM10[PM10[0.0:100.0,ug/m3];PM25[0.0:200.0,ug/m3];Temperatura[-20.0:50.0,°C];Humedad[0.0:100.0,%]"
    
    valores_regis = registros.values()
    for posi in valores_regis:
        fecha = posi[0]
        estacion = posi[1]
        medidas = posi[2]
        regis = fecha+";"+estacion+";"+medidas+"\n" 
        
        regis_nuevos += regis
        
    datos_nuevos = usu_nuevos+"\n"+muni_nuevos+"\n"+esta_nuevos+"\n"+parametros+"\n"+"\n"+regis_nuevos
    texto0 = open("registros_.txt", "w")
    texto0.write(datos_nuevos)        
        
def gestionar_usuario():
    datos = archivos("registros_.txt")
    usuarios = datos["usuarios"]
    caracteres_validos = "123"
    print("1. crear usuario")
    print("2. editar usuario")
    print("3. menu administrador")
    opcion = input("ingresar una opcion: ")
    while not opcion in caracteres_validos:
        opcion = input("ingrese una opcion correcta: ")
    if opcion == "1":
        print("crear usuario")
        while True:
            documento = input("ingrese el documento: ")
            validador1 = validar_documento(documento)
            if validador1 == True:
                if not documento in usuarios:
                    
                    break
            else:
                print("ingrese un documento valido") 
        while True:
            nombre = input("ingrese el nombre: ")
            validador2 = validar_nombre(nombre)
            if validador2 == True:
                break
            else:
                print("ingrese un nombre adecuado")
        while True:
            contraseña = input("ingresa una contraseña: ")
            validador3 = validar_contraseña(contraseña)
            if validador3 == True:
                break
            else:
                print("ingrese una contraseña valida")
        print("escoja un rol")
        print("1. administrador")
        print("2. operador")
        rol = input("ingrese un rol: ")
        while not rol in "12":
            rol = input("escoja una opcion valida: ")
        if rol == "1":
            rol ="Administrador"
        elif rol == "2":
            rol = "Operador"
        crear_usuario(documento,nombre,contraseña,rol)
        
    elif opcion == "2":
        print("editar usuario")
        editar_usuario()
    elif opcion == "3":
        administrador()
        
        
        
def editar_usuario():
    archivo = archivos("registros_.txt")
    usuarios = archivo["usuarios"]
    lista = []
    usuario = input("ingrese el documento del usuario a cambiar: ")
    while True:
        if usuario in usuarios:
            break
        else:
            usuario = input("ingrese un documento correcto: ")
    usuario_cambiar = usuarios[usuario]
    #nombre_antiguo = usuario_cambiar[1]
    print("el nombre actual es: ", usuario_cambiar[1],)
   
    nombre_nuevo = input("ingrese el nuevo nombre: ")
    validador = validar_nombre(nombre_nuevo)
    while True:
        if validador == True:
            break
        else: 
            nombre_nuevo = input("ingrese un nombre valido: ")
            validador = validar_nombre(nombre_nuevo)
    print("la contraseña actual es: ", usuario_cambiar[2])
    contra_otravez= ""
    contraseña = input("ingresar una contraseña: ")
    while contra_otravez != contraseña:
        while True:
            validador = validar_contraseña(contraseña)
            if validador == True:
                break
            else:
                contraseña = input("ingrese una contraseña valida: ")
                validador = validar_contraseña(contraseña)
        contra_otravez = input("ingrese de nuevo la contraseña: ")
        if contra_otravez == contraseña:
            break
        else:
            print("las contraseñas no coinciden")
    
    print("el rol actual es: ", usuario_cambiar[3])
    
    print("1. Administrador")
    print("2. Operador")
    rol = input("ingrese un nuevo rol: ")  
    while True:
        if rol in "12":
            break
        else:
            rol = input("ingrese una opcion valida. ")
    if rol == "1":
        nuevorol= "Administrador"
    else:
        nuevorol = "Operador"
    
               
    lista = [usuario, nombre_nuevo, contra_otravez, nuevorol]
    archivo["usuarios"][usuario] = lista
    cargar_datos(archivo)
    
    print("1. menu Administrador")
    print("2. salir del sistema")
    opcion = input("ingrese una opcion: ")
    while not opcion in "12":
        opcion= input("ingresar una opcion valida: ")
    if opcion == "1":
        administrador()
    elif opcion == "2":
        print("")
            
        #print(archivo)
            
#print(editar_usuario())
                        
        

    
    
def eliminar_usuario():
    """
    

    Parameters
    ----------
    def eliminar_usuario : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
        
def crear_usuario(documento, nombre, contraseña, rol):
    print(documento,nombre,contraseña,rol)
    datos = archivos("registros_.txt")
    usuarios = datos["usuarios"]
    lista_nuevo = []
    diccio_nuevo = {}
    lista_nuevo = [documento,nombre,contraseña,rol]
    diccio_nuevo[documento] = lista_nuevo
    usuarios.update(diccio_nuevo)
    cargar_datos(datos)
    
    print("1. menu Administrador")
    print("2. salir del sistema")
    opcion = input("ingrese una opcion: ")
    while not opcion in "12":
        opcion= input("ingresar una opcion valida: ")
    if opcion == "1":
        administrador()
    elif opcion == "2":
        print("")


        
            
def depuracion_de_registros():
    """
      """  

            
def editar_estacion():
    datos = archivos("registros_.txt")
    estaciones = datos["estaciones"]
    municipios = datos["municipios"]
    lista = []
        
       
    for valor in estaciones.values():
        lista.append(valor[1])
        contador = 1
    for j in lista:
        print(f"{contador}.{j}", end= "\n")
        contador += 1
        
    lista1 = []
    num = contador
    valido = False
    while not valido:
        try:
            eliminar = int(input("ingresar el numero de la estacion que desea eliminar: "))
            nueva = estaciones.get(str(eliminar))
            lista2 = []
            if nueva is not None:
                for valor in estaciones.values():
                    lista2.append(valor[1])
                    contador = 1
                for j in lista2:
                    print(f"{contador}.{j}", end= "\n")
                    contador += 1
                
                if eliminar > 0 and eliminar <= contador:
                    valido = True
                    nombre = input("ingresar un nuevo nombre: ")
                    nueva[1] = nombre
                    clave = "eliminar"
                    estaciones[clave] = nueva
                    print(nueva)
                    for valor in estaciones.values():
                        lista1.append(valor[1])
                        contador = 1
                    for j in lista1[:-1]:
                        print(f"{contador}.{j}", end= "\n")
                        contador += 1
                    
                    
                    
                    valido = False
                    while not valido:
                        try:
                           
                            print('\n'*20)
                            print("el municipio actual de la estacion es:", nueva[2])
                            lista4 = []
                            for valor in municipios:
                                lista4.append(valor)
                                contador = 1
                        
                    
                            for f in lista4[:-1]:
                                print(f"{contador}.{f}", end= "\n")
                                contador += 1
                            numero = int(input("ingresar el numero del municipio por el que desea cambiar el actual: "))
                            #numero -= 1
                            nueva = municipios.get(str(numero))
                            lista5 = []
                            if nueva is not None:
                                for valor in municipios.values():
                                    lista5.append(valor)
                                    contador = 1
                                for j in lista5[:-1]:
                                    print(f"{contador}.{j}", end= "\n")
                                    contador += 1
                
                                if numero > 0 and numero <= contador:
                                    valido = True
                                    nombre = lista5[numero]
                                    nueva[2] = nombre                                   
                                    clave = "nombre"
                                    estaciones[clave] = nueva
                                    print(estaciones)
                                    
                            else:
                                print("la clave no existe, intentalo de nuevo")
                        except ValueError:
                            print("debe ingresar un numero")
                            
                    
            
                    
                                    
            else:
                print("la clave no existe, intentalo de nuevo")
        except ValueError:
            print("debe ingresar un numero")
            
            
            
        
    
    
    
    #print(nueva)
#print(editar_estacion())    
                    
def eliminar_estacion():
    """
    

    Returns
    -------
    None.

    """
    
    

    
            
            
           
#print(Gestionar_estaciones())

def verificar_numero(valor,lista):
    if valor > len(lista) or valor < 1:
        return False
    return True

    
def visitante():
    """
    

    Returns
    -------
    None.

    """



def validar_fecha(fecha):
    '''
    Valida que un string corresponda a una fecha válida (con formato yyyy-mm-dd).
    
    Argumentos:
        fecha -> string a validar
    return -> Boolean (True or False) si es valido o no
    '''
    año = ""
    mes = ""
    dia = ""
    
    Nseparadores = split(fecha , "-")
    if len(Nseparadores) != 3:
        return False 
    
    
    try:
        año = int(Nseparadores[0])
        mes = int(Nseparadores[1])
        dia = int(Nseparadores[2])
        
    except ValueError:
        return False 
   
   
    
    if año < 1 or mes < 1 or mes > 12 or dia < 1 or dia > 31:
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2:
        if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
            if dia > 29 :
                return False
        else : 
            if dia > 28:
                return False
    
    return True
    
    pass

def limpiar_pantalla():
    '''
    Imprime varias líneas en blanco, para dar la ilusión 
    de limpiar la pantalla
    '''
    print('\n'*20)

def imprimir_tabla(tabla, ancho, encabezado=None):  
    ''' 
    Imprime en pantalla un tabla con los datos pasados, ajustado a los tamaños deseados.
    
    Argumentos:
        tabla: Lista que representa la tabla. Cada elemento es una fila
        ancho: Lista con el tamaño deseado para cada columna. Si se especifica
            un entero, todas las columnas quedan de ese tamaño
        encabezado: Lista con el encabezado de la tabla
    '''
    def dividir_fila(ancho,sep='-'):
        '''
        ancho: Lista con el tamaño de cada columna
        se: Caracter con el que se van a formar las líneas que 
            separan las filas
        '''
        linea = ''
        for i in range(len(ancho)):
            linea += ('+'+sep*(ancho[i]-1))
        linea = linea[:-1]+'+'
        print(linea)
        
    def imprimir_celda(texto, impresos, relleno):
        '''
        texto: Texto que se va a colocar en la celda
        impresos: cantidad de caracteres ya impresos del texto
        relleno: cantidad de caracteres que se agregan automáticamente,
            para separar los textos del borde de las celda.
        '''        
        # Imprimir celda
        if type(texto) == type(0.0):
            #print(texto)
            texto = '{:^7.2f}'.format(texto)
            #print(type(texto), texto)
        else:
            texto = str(texto)
        texto = texto.replace('\n',' ').replace('\t',' ')
        if impresos+relleno < len(texto):
            print(texto[impresos:impresos+relleno],end='')
            impresos+=relleno
        elif impresos >= len(texto):
            print(' '*(relleno),end='')
        else:
            print(texto[impresos:], end='')
            print(' '*(relleno-(len(texto) - impresos)),end='')
            impresos = len(texto)
        return impresos
    
    def imprimir_fila(fila):
        '''
        fila: Lista con los textos de las celdas de la fila
        '''
        impresos = []   
        alto = 1
        for i in range(len(fila)):
            impresos.append(0)
            if type(fila[i]) == type(0.0):
                texto = '{:7.2f}'.format(fila[i])
            else:
                texto = str(fila[i])
            alto1 = len(texto)//(ancho[i]-4)
            if len(texto)%(ancho[i]-4) != 0:
                alto1+=1
            if alto1 > alto:
                alto = alto1
        for i in range(alto):
            print('| ',end='')
            for j in range(len(fila)):
                relleno = ancho[j]-3
                if j == len(fila)-1:
                    relleno = ancho[j] -4
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' |')
                else:
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' | ',end='')   
    if not len(tabla) > 0:
        return
    if not type(tabla[0]) is list:
        return
    ncols = len(tabla[0])
    if type(ancho) == type(0):
        ancho = [ancho+3]*ncols 
    elif type(ancho) is list:
        for i in range(len(ancho)):
            ancho[i]+=3
    else:
        print('Error. El ancho debe ser un entero o una lista de enteros')
        return
    assert len(ancho) == ncols, 'La cantidad de columnas no coincide con los tamaños dados'
    ancho[-1] += 1
    if encabezado != None:
        dividir_fila(ancho,'=')
        imprimir_fila(encabezado)
        dividir_fila(ancho,'=')
    else:
        dividir_fila(ancho)
    for fila in tabla:
        imprimir_fila(fila)
        dividir_fila(ancho)
