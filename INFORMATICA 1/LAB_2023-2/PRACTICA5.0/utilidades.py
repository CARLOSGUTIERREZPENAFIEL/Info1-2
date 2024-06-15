from datetime import*

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
        

#imprimir_tabla([['Dato1', 'Dato2', 'Temperatura', 'Humedad'],['.15', '', '16', '-19.9', '-999']], 12)      

def eliminar_diccionario(diccionario, key):

    nuevo_diccionario = {}
    for clave in diccionario:
        if clave != key:
            nuevo_diccionario[clave] = diccionario[clave]
    return nuevo_diccionario
    
def validar_documento2(documento, otro):
    num_validos = "0123456789"

    if len(documento) != 10:
        return False
    elif documento not in otro:
        return False
    for i in documento:
        if i not in num_validos:
            return False
    return True

def validar_documento(documento, otro):
    num_validos = "0123456789"

    if len(documento) != 10:
        return False
    elif documento in otro:
        return False
    for i in documento:
        if i not in num_validos:
            return False
    return True
#print(validar_documento("1234",["1234567890", "0987654321"]))
def validar_contra(key):
    key_valido = "0123456789"
    if len(key) != 4:
        return False
    for i in key:
        if i not in key_valido:
            return False
    return True
def validar_nombre(nombre):
    import string
    
    
    abc = string.ascii_lowercase
    abc = abc + abc.upper() + " "
    
    for i in nombre:
        if i not in abc:
            return False
    return True
def cargar_datos(datos):
    usu_nuevos = ""
    esta_nuevos = ""
    regis_nuevos = ""
    muni_nuevos = ""
    muni = ""
    usuarios = datos["usuarios"]
    estaciones = datos["estacion"]
    registros = datos["registro"]
    municipios = datos["municipio"]
    
    valores_usu = usuarios.values()
    for posi in valores_usu:
        docu = posi[0]
        nomb = posi[1]
        clave = posi[2]
        traba = posi[3]
        usu = "<"+docu+";"+nomb+";"+clave+";"+traba+">"+"\n"
        usu_nuevos += usu
    muni = ",".join(municipios)
    muni_nuevos = ":"+muni+"\n"
    
    valores_estaciones = estaciones.values()
    for posi in valores_estaciones:
        valor = posi[0]
        lugar = posi[1]
        municipio = posi[2]
        esta = valor+","+lugar+","+municipio+"\n"
        esta_nuevos += esta
    parametros = datos["resto"]+ "\n"
    
    valores_regis = registros.values()
    for posi in valores_regis:
        fecha = posi[0]
        estacion = posi[1]
        medidas = posi[2]
        regis = fecha+";"+estacion+";"+medidas+"\n" 
        
        regis_nuevos += regis
        
    datos_nuevos = usu_nuevos+muni_nuevos+esta_nuevos+"".join(parametros)+regis_nuevos
    texto0 = open("registros_v2.txt", "w")
    texto0.write(datos_nuevos)        
    #print( datos_nuevos)
#cargar_datos({'usuarios': {'1010101010': ['1010101010', 'Mariana Montoya', '1234', 'Administrador'], '1111111111': ['1111111111', 'Elkin Perez', '1234', 'Operador'], '1212121212': ['1212121212', 'Camila Serna', '1234', 'Administrador'], '1313131313': ['1313131313', 'Oscar Jaramillo', '1234', 'Operador']}, 'municipio': ['Medellin', 'Bello', 'Itagui', 'Caldas', 'La Estrella', 'Barbosa'], 'estacion': {'1': ['1', 'Universidad San Buenaventura', 'Medellin'], '2': ['2', 'I.E. Concejo Municipal de Itagui', 'Itagui'], '3': ['3', 'E U JoaquÃ\xadn Aristizabal', 'Caldas'], '4': ['4', 'Hospital', 'La Estrella'], '5': ['5', 'Torre Social', 'Barbosa'], '6': ['6', 'Parque principal', 'Caldas']}, 'resto': ['PM10[0.0:100.0,ug/m3]', 'PM25[0.0:200.0,ug/m3]', 'Temperatura[-20.0:50.0,Â°C]', 'Humedad[0.0:100.0,%]'], 'registro': {'1': ['2019-07-01 00:00:00', '1', '{3.5,6.2,27.0,34.0}'], '2': ['2019-07-01 00:10:00', '2', '{8.1,-999.0,29.0,37.0}'], '3': ['2019-07-01 00:00:00', '3', '{7.9,-999.0,31.0,-999.0}'], '4': ['2019-04-01 00:00:00', '4', '{-999.0,6.4,-999.0,41.0}']}})      
def leer_archivo(fileName):
    leer = open(fileName, "r")
    diccionario_usuario = {}
    diccionario_estacion = {}
    diccionario_registro = {}
    for line in leer:
        line = line.strip()
        if not line:
            continue
        if line[0] == "<":
            line = line[1:-1]
            usuario = line.split(";")
            diccionario_usuario[usuario[0]]= usuario
        elif line[0] == ":":
            line = line[1:]
            municipio = line.split(",")
        elif line[1] == ",":
            estacion = line.split(",")
            diccionario_estacion[estacion[0]] = estacion
        elif line[4] == "-":
            registro = line.split(";")
            diccionario_registro[registro[1]] = registro
        else:
            resto = line
    diccionario_global = {"usuarios":diccionario_usuario, "municipio": municipio, "estacion": diccionario_estacion, "resto": resto, "registro": diccionario_registro}
    return diccionario_global
#print(leer_archivo("registros_.txt")) 
            
            
#print(leer_archivo("copia.txt"))         
def visualizar_estadisticas():
    print("\n"*30)                 
    datos=leer_archivo('registros_v2.txt')
    registros=datos['registro']
    estaciones=datos['estacion']
    parametros = datos["resto"]
    escoger=estaciones.values()
    for i in escoger:
        estacion = i[0]
        lugar=i[1]
        municipio=i[2]
        print(estacion, lugar, municipio)
          
    
    numero=input('ingrese el número de la estación: ')
    encabezado=['fecha','estación','medidas']
    lista_tabla=[]
    lista_registros=registros.values()
    for regis in lista_registros:
        
        if regis[1]==numero:
            lista_tabla.append(regis)
            
    print('PARAMETROS DE MEDIDA: ')        
    print(parametros)
                
    imprimir_tabla(lista_tabla, 25,encabezado)
    visitante()
    
def visitante():
    print("\n"*30)
    print("**USUARIO VISITANTE**")
    opcion = input("1. Visualizar estadisticas \n2. Menu principal \n")
    while True:
        if opcion == "1":
            visualizar_estadisticas()
            break
        elif opcion == "2":
            menu()
            break
        else:
            opcion = input("ingrese una opcion valida: \n")
            

def mostrar_medidas(estacion_principal):
    lista = []
    lista2 = ["Dato1","Dato2","Temperatura","Humedad"]
    lista.append(lista2)
    archivo = leer_archivo("registros_v2.txt")
    estacion = archivo["estacion"]
    for i in estacion:
        if estacion[i][1] == estacion_principal:
            num_estacion = estacion[i][0]
    datos = archivo["registro"]
    
    registro = datos[num_estacion]
    #print(registro[0])
    #a = regitro[2]
    lista1 = registro[2][1:-1].split(",")
    lista.append(lista1)
    #print(lista1)
    print(lista)
    print("fecha: ", registro[0])
    imprimir_tabla(lista, 15)
    
    opcion = input("1. volver al menu principal \n2. menu operador \n")
    while True:
        if opcion == "1":
            menu()
            break
        elif opcion == "2":
            operador()
        else:
            opcion = input("imgrese una opcion valida: \n")
            
#mostrar_medidas("Universidad San Buenaventura")
def validar_dato(dato):
    try:
        float(dato)
        return True
    except:
        return False
    
def validar_parametro(dato,minimo, maximo):
    aux = validar_dato(dato)
    while True:
        if aux == False:
            dato = input("ingresar un dato valido: \n")
            aux = validar_dato(dato)
        elif float(dato)>= float(minimo) and float(dato)<= float(maximo):
            return True,dato
        else:
            return False, ""
    
def ingresar_medidas(estacion_principal,numero):
    archivo = leer_archivo("registros_v2.txt")
    parametro = archivo["resto"]
    estacion = archivo["estacion"]
    registro = archivo["registro"]
    parametro_aux = parametro[:]
    diccionario_parametros = {}

    

    while True:
        x = parametro_aux.find("[")
        y = parametro_aux.find("]")
        z = parametro_aux.find(",")
        clave = parametro_aux[:x]
        valor = parametro_aux[x+1:z]
        valor = valor.split(":")        
        
        diccionario_parametros[clave]= valor
        parametro_aux = parametro_aux[y+1:]
        if parametro_aux =="":
            break
        

    dato1 = input("Ingrese el valor PM10: \n").lower()
    minimo = diccionario_parametros["PM10"][0]
    maximo = diccionario_parametros["PM10"][1]
    if dato1 != "nd": 
        aux,dato1 = validar_parametro(dato1, minimo, maximo)
        while aux == False:
            dato1 = input("ingrese un dato dentro de los parametros: \n").lower()
            aux,dato1 = validar_parametro(dato1, minimo, maximo)
    else:
        dato1 = "-999"
    
  
    dato2 = input("Ingrese el valor PM25: \n")
    minimo = diccionario_parametros[";PM25"][0]
    maximo = diccionario_parametros[";PM25"][1]
    if dato2 != "nd": 
        aux,dato2 = validar_parametro(dato2, minimo, maximo)
        while aux == False:
            dato2 = input("ingrese un dato dentro de los parametros: \n").lower()
            aux,dato2 = validar_parametro(dato2, minimo, maximo)
    else:
        dato2 = "-999"
        
    temperatura = input("Ingrese el valor de la temperatura: \n").lower()
    minimo = diccionario_parametros[";Temperatura"][0]
    maximo = diccionario_parametros[";Temperatura"][1]
    if temperatura != "nd": 
        aux,temperatura = validar_parametro(temperatura, minimo, maximo)
        while aux == False:
            temperatura = input("ingrese un dato dentro de los parametros: \n").lower()
            aux,temperatura = validar_parametro(temperatura, minimo, maximo)
    else:
        temperatura = "-999"
    
    humedad = input("Ingrese el valor de la humedad: \n").lower()
    minimo = diccionario_parametros[";Humedad"][0]
    maximo = diccionario_parametros[";Humedad"][1]
    if humedad != "nd": 
        aux,humedad = validar_parametro(humedad, minimo, maximo)
        while aux == False:
            humedad = input("ingrese un dato dentro de los parametros: \n").lower()
            aux,humedad = validar_parametro(humedad, minimo, maximo)
    else:
        humedad = "-999"
    
        
    
    lista_nueva = []
    time =str(datetime.now())
    aux = time.find(".")
    time = time[:aux]
    nuevo = time +";"+numero+";"+"{"+dato1+","+dato2+","+temperatura+","+humedad+"}"
    nuevo = nuevo.split(";")
    registro[numero] = nuevo
    cargar_datos(archivo)
    operador()
#ingresar_medidas("E U JoaquÃ­n Aristizabal", "2")    

def operador():
   
    print("\n"*30)
    print("**USUARIO OPERADOR**")
    archivo = leer_archivo("registros_v2.txt")
    estacion = archivo["estacion"]
    municipio = archivo["municipio"]
    registro = archivo["registro"]
    lista_estacionesV = []
    lista_muniValidos = []
    lista_esta_muni= []
    for i in registro:
        lista_esta_muni.append(registro[i][1])
    opcion1 = input("1. Seleccionar el municipio en que esta ubicada la estacion \n2. volver al menu principal \n")
    for i in estacion:
        if i not in lista_muniValidos:
            lista_muniValidos.append(estacion[i][2])
    while True:
        if opcion1 == "1":
            break
        elif opcion1 == "2":
            menu()
            break
        else:
            opcion1= input("selecciones una opcion valida: \n")
    for i in municipio:
        print("-",i)
    opcion_muni = input("Escriba el nombre del municipio: \n")
    while True:
        if opcion_muni not in lista_muniValidos:
            opcion_muni = input("este municipio no tiene estaciones asociadas, escriba otro: \n")
        else:
            break
    print("\n"*30)
    opcion2 = input("1. Selecionar la estacion del listado de estaciones correspondientes al municipio seleccionado \n2. volver a la opcion de elegir municipio \n")
    while True:
        if opcion2 == "1":
            break
        elif opcion2 == "2":
            operador()
            break
        else:
            opcion2= input("Seleccionar una opcion valida")
    for i in estacion:
        if estacion[i][2] == opcion_muni:
            lista_estacionesV.append(estacion[i][1])
            print("-",estacion[i][1])
    opcion_estacion = input("Escriba una estacion de la lista: \n")
    while True:
        if opcion_estacion not in lista_estacionesV:
            opcion_estacion = input("Escriba una estacion valida: \n")
        else:
            break
    for i in estacion:
        if estacion[i][1] == opcion_estacion:
            numero_esta = estacion[i][0]
    print("\n"*30)
    opcion3 = input("1. mostrar medidas \n2. ingresar medidas \n")
    while True:
        if opcion3  == "1":
            if numero_esta not in lista_esta_muni:
                print("Esta estacion no tiene medidas")
                for i in estacion:
                    if estacion[i][2] == opcion_muni:
                        lista_estacionesV.append(estacion[i][2])
                        print("-",estacion[i][1])
                opcion_estacion = input("Escriba una estacion de la lista o escriba 3 para volver al menu operador: \n").lower().capitalize()
                while True:
                    if opcion_estacion == "3":
                        operador()
                        break
                    elif opcion_estacion not in lista_estacionesV:
                        opcion_estacion = input("Escriba una estacion valida: \n")
                    
                    else:
                        break
                for i in estacion:
                    if estacion[i][1] == opcion_estacion:
                        numero_esta = estacion[i][0]
            else:
                mostrar_medidas(opcion_estacion)
                break
        elif opcion3 == "2":
            ingresar_medidas(opcion_estacion, numero_esta)
            break
        else:
            opcion3 = input("Ingrese una opcion valida: \n")
            
#operador()
def editar_estacion(cedula):
    print("\n"*30)
    print("**EDITAR ESTACIONES**")
    archivo= leer_archivo('registros_v2.txt')
    estaciones = archivo['estacion']
    municipios= archivo['municipio']
    for key in estaciones:
        numero = estaciones[key][0]
        estacion = estaciones[key][1]
        lista = numero + ". " + estacion
        print(lista)
    editar= input('Que estacion deseas editar: \n')
    listavalidacion=[]
    for key in estaciones:
        listavalidacion.append(estaciones[key][0])
    while True:
        for numero in listavalidacion:
            if editar in listavalidacion:
                valor=True
            else:
                editar= input('Digite una estacion valida: \n')
        if valor==True:
            break
    aux = ", ".join(estaciones[editar])
    print(aux)
    YoN= input('Desea editar esta estacion: Y o N \n').lower()
    while True :
        if YoN=='y':
            break
        elif YoN=='n':
            break
        else:
            YoN=input('Ingrese una opcion valida:\n').lower()
    if YoN == 'y':
        nueva_estacion=input('Cual es el nuevo nombre de la estacion:\n').lower()
        validacion_nombre= validar_nombre(nueva_estacion)
        while validacion_nombre== False:
            nueva_estacion=input('Digite Un Nombre Correcto:\n').lower()
            validacion_nombre= validar_nombre(nueva_estacion)
        nlista=(estaciones[editar])[:]
        nlista[1]= nueva_estacion
        YoN=input('Deseas cambiar de muncipio Y o N:\n').lower()
        while True :
            if YoN=='y':
                break
            elif YoN=='n':
                break
            else:
                YoN=input('Ingrese una opcion valida:\n')
        if YoN=='y':
            print('Municipios disponibles:')
            i=1
            for key in municipios:
                print(i , key)
                i+=1
            nueva_municipio= int(input('Elige la opcion a cual municipio se desea mudar la estacion:\n'))
            nlista[2]= municipios[nueva_municipio-1]
        else:
            nlista
    else:
        editar_estacion()
    estaciones[editar]=nlista
    archivo['estacion']= estaciones
    cargar_datos(archivo)
    gestionar_estaciones(cedula)
#print(editar_estacion())

def menu():
    print("\n"*30)
    print("MENU")
    print("1. usuario registrado")
    print("2. usuario visitante")
    print("3. salir del sistema")
    
    opcion = (input("seleccionar una opcion: "))
    caracteres_validos = "123"
    while not opcion in caracteres_validos:
        opcion = (input("ingrese un caracter correcto: \n"))
    
    if opcion == "1":
        registrado()
    elif opcion == "2":
        visitante()
    elif opcion =="3":
        print("")
        
def estaciones_invalidas(archivo):
    estaciones_invalidas=[]
    for key in archivo:
        estacion= archivo[key][1]
        estaciones_invalidas.append(estacion)
    return estaciones_invalidas

def mostrar_estaciones(archivo):
    opciones=[]
    for key in archivo:
        opciones.append(archivo[key][0])
        numero = archivo[key][0]
        estacion = archivo[key][1]
        lista = numero + ". " + estacion
        print(lista)
    print('-'*40)
    return opciones
def confirmacion(YoN):
    while True :
        if YoN=='y':
            return YoN
        elif YoN=='n':
            return YoN
        else:
            YoN=input('Ingrese una opcion valida:\n')

def eliminar_estacion(cedula):
    print("\n"*30)
    print("**ELIMINAR ESTACION**")
    archivo= leer_archivo('registros_v2.txt')
    registros = archivo["registro"]
    estaciones = archivo['estacion']
    estacion_invalida= estaciones_invalidas(registros)
    aux= str(mostrar_estaciones(estaciones))
    eliminar= input('Que Estacion Desea Eliminar:\n')
    while True:
        if eliminar in aux:
            if eliminar not in estacion_invalida:
                break
            else:
                print("Esta Estacion Tiene Datos Asociados \n")
                #eliminar= (input('Esta Estacion Tiene Datos Asociados, Ingrese Otra:\n'))
                
                while True:
                    opcion = input("1. Intentar de nuevo \n2. volver a Gestionar Usuarios \n")
                    if opcion == "1":
                        eliminar= (input('Que estacion desea eliminar:\n'))
                    elif opcion == "2":
                        gestionar_usuarios(cedula)
                    
        else:
            eliminar= (input('Ingrese Una Opcion Valida:\n'))
    nlista= estaciones[eliminar][:]
    print('\n--SE ELIMINARA ESTA ESTACION--\nEstacion:', nlista[1])
    YoN= input('Desea Eliminar Estacion: Y o N:\n')
    aux= confirmacion(YoN)
    if aux== 'y':
        estaciones= eliminar_diccionario(estaciones, eliminar)
        print("\n --SE ELIMINO LA ESTACION-- \n", nlista[1])
        archivo["estacion"]= estaciones
        cargar_datos(archivo)
        gestionar_estaciones(cedula)
    else:
        gestionar_estaciones(cedula)
    
    
#eliminar_estacion()

def crear_estacion(cedula):
    print("\n"*30)
    print("**CREAR ESTACION**")
    archivo= leer_archivo("registros_v2.txt")
    estacion = archivo["estacion"]
    municipio = archivo["municipio"]
    cont = 0
    numero = 0
    nueva_estacion = input("ingresar el nombre de la nueva estacion: \n").lower()
    for i in estacion:
        cont += 1
    for i in range(0, len(municipio)):
         numero += 1
         print(numero,".",municipio[i])
    nuevo_municipio = int(input("ingrese el municipio del listado: \n ")) 
    while True:
         if nuevo_municipio > numero or nuevo_municipio <= 0:
             nuevo_municipio = int(input("ese numero no tiene asignado un municipio, ingrese uno valido: \n"))
         else:
             break
    key = str(cont+1)
    estacion[key] = [key, nueva_estacion, municipio[nuevo_municipio-1]]
    cargar_datos(archivo)
    gestionar_estaciones(cedula)
    
#print(crear_estacion())
def crear_usuario(cedula):
    print("\n"*30)
    print("**CREAR USUARIOS**")
    archivo = leer_archivo("registros_v2.txt")
    usuarios = archivo["usuarios"]
    lista_doc = []
    for i in usuarios:
        lista_doc.append(usuarios[i][0])
    documento = input("ingresar el numero de documento: \n")
    validar = validar_documento(documento, lista_doc)
    while validar == False:
        documento= input("por favor ingresar documento valido: \n")
        validar = validar_documento(documento, lista_doc)
    nombre = input("ingresar el nombre: \n").lower()
    aux_nombre = validar_nombre(nombre)
    while aux_nombre == False:
        nombre = input("ingresar un nombre valido: \n").lower()
        aux_nombre = validar_nombre(nombre)
    contra = input("crear contraseña: \n")
    aux_key = validar_contra(contra)
    while aux_key == False:
        contra = input("ingrese una contraseña valida: \n")
        aux_key = validar_contra(contra)
    confirmar = input("por favor confirme la contraseña: \n")
    while True:
        if contra != confirmar:
            confirmar = input("por favor confirme bien la contraseña: \n")
        else:
            break
    rol = input("1. Administrador \n2. Operador \nSeleccionar el rol para el usuario: \n")
    while True:
        if rol == "1":
            rol = "Administrador"
            break
        elif rol == "2":
            rol = "Operador"
            break
        else:
            rol = input("ingrese una opcion valida: \n")
    usuarios[documento] = [documento,nombre,contra,rol]
    cargar_datos(archivo)
    gestionar_usuarios(cedula)
    #print(archivo)
#crear_usuario()
def opciones_validas(numero):
    opciones_validas=["1","2","3","4"]
    while True:
        if numero in opciones_validas:
            return int(numero)
        else:
            numero= input('Ingrese una opcion valida:\n')
 
def cedulas_valida(usuarios):
    cedulas_validas=[]
    for key in usuarios:
        cedula= usuarios[key][0]
        cedulas_validas.append(cedula)
    return cedulas_validas

def mostrar_usuarios(archivo):
    opcion=1
    for key in archivo:
         cedula= archivo[key][0]
         nombre= archivo[key][1]
         contraseña=archivo[key][2]
         funcion=archivo[key][3]
         lista= '\n'+str(opcion)+ '. Cedula:'+cedula+ ' Nombre:'+nombre +' Contraseña:'+contraseña+ ' Rol:'+funcion
         opcion+=1
         print(lista)
    print('-'*45) 
    return opcion

def opciones_validas_usuarios(opcion,validar):
    cont=1
    opciones_validas=[]
    while cont<opcion:
        opciones_validas.append(str(cont))
        cont+=1
    while True:
        if validar in opciones_validas:
            return int(validar)
        else:
            validar= input('Ingrese una opcion valida:\n')
            
def validacion_documento(documento):
    digitos_validos= '1234567890'
    for num in documento:
        if num not in digitos_validos:
            return False
    if len(documento) !=10:
        return False
    return True

  
def editar_usuario(cedula):
     print("\n"*30)
     print("**EDITAR USUARIO**")
     archivo= leer_archivo('registros_v2.txt')
     usuarios = archivo["usuarios"]
     print('**OPCIONES PARA EDITAR USUARIO**')
     print('1. Editar Cedula\n2. Editar Nombre\n3. Editar Contraseña \n4. Editar Rol ')
     opcion= input("Ingrese una Opcion:\n")
     aux=opciones_validas(opcion)
     if aux == 1:
         cedulas_validas= cedulas_valida(usuarios)
         aux= mostrar_usuarios(usuarios)
         editar= input('Que usuario desea editar:\n')
         editar=opciones_validas_usuarios(aux, editar)
         cedula_editar= cedulas_validas[editar-1]
         nlista= (usuarios[cedula_editar])[:]
         print('\n--CEDULA ACTUAL--\n', nlista[0], '\n')
         nueva_cedula= input('Ingrese la nueva Cedula:\n')
         validar_doc= validacion_documento(nueva_cedula)
         while validar_doc== False:
             nueva_cedula= input('Ingrese Una Cedula Valida:\n')
             validar_doc= validacion_documento(nueva_cedula)
         Confirmar_Cedula= input('Ingrese Nuevamente la Cedula Para Confirmar:\n')
         while True:
             if nueva_cedula==Confirmar_Cedula:
                 break
             else:
                 print('\n**ERROR**\nLas Cedulas son Diferentes\n')
                 nueva_cedula= input('Ingrese la nueva Cedula:\n')
                 validar_doc= validacion_documento(nueva_cedula)
                 while validar_doc== False:
                     nueva_cedula= input('Ingrese Una Cedula Valida:\n')
                     validar_doc= validacion_documento(nueva_cedula)
                 Confirmar_Cedula= input('Ingrese Nuevamente la Cedula Para Confirmar:\n')
         nlista[0]=nueva_cedula
         usuarios[cedula_editar]=nlista
         archivo["usuarios"] = usuarios
         cargar_datos(archivo)
         gestionar_usuarios(cedula)
     elif aux == 2:
         cedulas_validas= cedulas_valida(usuarios)
         print('**EDITAR NOMBRE**\nUSUARIOS DISPONIBLES')
         aux= mostrar_usuarios(usuarios)
         editar= input('Que usuario desea editar:\n')
         editar=opciones_validas_usuarios(aux, editar)
         nombre_editar= cedulas_validas[editar-1]
         nlista= (usuarios[nombre_editar])[:]
         print('--NOMBRE ACTUAL--\n', nlista[1],'\n')
         nuevo_nombre= input('Ingrese el Nuevo Nombre:\n').lower()
         validacion_nombre=validar_nombre(nuevo_nombre)
         while validacion_nombre == False:
             nuevo_nombre= input('Ingrese Un Nombre Valido:\n').lower()
             validacion_nombre= validar_nombre(nuevo_nombre)
         nlista[1]= nuevo_nombre
         usuarios[nombre_editar]=nlista
         archivo["usuarios"] = usuarios
         cargar_datos(archivo)
         gestionar_usuarios(cedula)
     elif aux == 3:
         cedulas_validas= cedulas_valida(usuarios)
         print('**EDITAR Contraseña**\nUSUARIOS DISPONIBLES')
         aux= mostrar_usuarios(usuarios)
         editar= input('Que usuario desea editar:\n')
         editar=opciones_validas_usuarios(aux, editar)
         contraseña_editar= cedulas_validas[editar-1]
         nlista= (usuarios[contraseña_editar])[:]
         print('\n--CONTRASEÑA ACTUAL--\n',nlista[2],'\n')
         nueva_contraeña= input('Ingrese la nueva Contraseña:\n')
         validar_cont = validar_contra(nueva_contraeña)
         while validar_cont == False:
             nueva_contraeña = input("Ingrese una contraseña valida: \n")
             validar_cont = validar_contra(nueva_contraeña)
         Confirmar_Contraseña= input('Ingrese Nuevamente la Contraseña:\n')
         while True:
             if nueva_contraeña==Confirmar_Contraseña:
                 break
             else:
                 print('\n**ERROR** Las Contraseñas son Diferentes\n')
                 nueva_contraeña= input('Ingrese la nueva Contraseña:\n')
                 validar_cont = validar_contra(nueva_contraeña)
                 while validar_cont == False:
                     nueva_contraeña = input("Ingrese una contraseña valida: \n")
                     validar_cont = validar_contra(nueva_contraeña)
                 Confirmar_Contraseña= input('Ingrese Nuevamente la Contraeña:\n') 
         nlista[2]=nueva_contraeña
         usuarios[contraseña_editar]=nlista
         archivo["usuarios"] = usuarios
         cargar_datos(archivo)
         gestionar_usuarios(cedula)
     elif aux == 4:
         cedulas_validas= cedulas_valida(usuarios)
         print('**EDITAR ROl**\nUSUARIOS DISPONIBLES')
         aux= mostrar_usuarios(usuarios)
         editar= input('Que usuario desea editar:\n')
         editar=opciones_validas_usuarios(aux, editar)
         rol_editar= cedulas_validas[editar-1]
         nlista= (usuarios[rol_editar])[:]
         print('\n--ROL ACTUAL--\n', nlista[3],'\n')
         print('**ROLES DISPONIBLES**\n1. Administrador\n2. Operador\n')
         nuevo_rol= (input('Ingrese la Opcion del Nuevo Rol:\n'))
         while True:
             if nuevo_rol == '1' or nuevo_rol == '2':
                 break
             else:
                 nuevo_rol= input('Ingrese Una Opcion Valida:\n')
         roles= ['Administrador','Operador']
         nlista[3]= roles[int(nuevo_rol)-1]
         usuarios[rol_editar]=nlista
         archivo["usuarios"] = usuarios
         cargar_datos(archivo)
         gestionar_usuarios(cedula)
     
#print(editar_usuario())

def eliminar_usuario(cedula):
    print("\n"*30)
    print("**ELIMINAR USUARIOS**")
    archivo = leer_archivo("registros_v2.txt")
    usuarios = archivo["usuarios"]
    cedulas = []
    for i in usuarios:
        if i != cedula:
            cedulas.append(usuarios[i][0])
            print("-", usuarios[i][0], "-", usuarios[i][1])
    documento = input("Ingresar el documento del usuario que desea eliminar: \n")
    aux = validar_documento2(documento,cedulas)
    while aux == False:
        documento = input("ingresar un documento valido: \n")
        aux = validar_documento2(documento, cedulas)
    print("Desea eliminar el usuario con el numero de documento: ", documento)
    confirmar = input("Y o N: \n").lower()
    while True:
        if confirmar == "y":
            break
        elif confirmar == "n":
            print("no se elimino")
            gestionar_usuarios(cedula)
        else:
            confirmar = input("ingresar una opcion valida, Y o N \n").lower()
    usuarios = eliminar_diccionario(usuarios, documento)
    archivo["usuarios"] = usuarios
    cargar_datos(archivo)
    gestionar_usuarios(cedula)
    
#print(eliminar_usuario("1044211634"))
    
def gestionar_estaciones(cedula):
    print("\n"*30)
    print("**GESTIONAR ESTACIONES**")
    opcion = input("seleccione una opcion: \n1.crear estacion \n2. Editar estacion \n3. Eliminar estacion \n4. Menu Administrador \n")  
    while True:
        if opcion == "1":
            crear_estacion(cedula)
            break
        elif opcion == "2":
            editar_estacion(cedula)
            break
        elif opcion == "3":
            eliminar_estacion(cedula)
            break
        elif opcion == "4":
            administrador(cedula)
            break
        else:
            opcion = input("ingrese una opcion valida: \n")
            
        
def gestionar_usuarios(cedula):
    print("\n"*30)
    print("**GESTIONAR USUARIOS**")
    opcion = input("1. Crear usuario \n2. Editar usuario \n3. Eliminar usuario \n4. Menu Administrador \nIngrese una opcion: \n")
    while True:
        if opcion == "1":
            crear_usuario(cedula)
            break
        elif opcion == "2":
            editar_usuario(cedula)
            break
        elif opcion == "3":
            eliminar_usuario(cedula)
            break
        elif opcion == "4":
            administrador(cedula)
            break
        else:
            opcion = input("ingrese una opcion valida: \n")
            

#depuracion_registros("1111111111")


def administrador(cedula):
    print("\n"* 30)
    print("**USUARIO ADMINISTRADOR**")
    print("1. Volver al menu inicial \n2. Gestionar estaciones \n3. Gestionar usuario \n4. Depuracion de registros ")
    opcion = input("ingrese una opcion: \n")
    valido = "12345"
    while True:
        if opcion not in valido:
           opcion = input("ingrese una opcion: \n") 
        else:
            break
    if opcion == "1":
        menu()
        
            
    elif opcion == "2":
        gestionar_estaciones(cedula)
    elif opcion == "3":
        gestionar_usuarios(cedula)
    elif opcion == "4":
        depuracion_registros(cedula)
    
        
def registrado():
    archivo = leer_archivo("registros_v2.txt")
    usuarios = archivo["usuarios"]
    nada = ""
    cedula = input("ingrese su documento: \n")
    aux= validar_documento(cedula, nada)
    lista_documentos = []
    for i in usuarios:
        lista_documentos.append(i)
    while aux == False:
        cedula = input("ingrese un documento valido: \n")
        aux= validar_documento(cedula,nada)
    while True:
        if cedula not in lista_documentos:
            opcion = input("la cedula ingresada no se encuentra en el sistema \n 1. volver al menu inicial \n 2. intentar con otra cedula \n")
            while True:
                if opcion == "1":
                    menu()
                    break
                elif opcion == "2":
                    cedula = input("ingrese su documento: \n")
                    break
                else:
                    opcion = input("ingrese una opcion valida: \n")
        break
    key_original = usuarios[cedula][2]
    contra = input("ingrese la contraseña: \n")
    intentos = 3
    while True:
        if key_original != contra:
            contra = input("contraseña incorrecta: ")
            intentos-= 1
            print("tiene ", intentos, "intentos")
            if intentos == 0:
                print("intentos agotados")
                menu()
                break
        else:
            break
    
    if usuarios[cedula][3] == "Operador":
        operador()
    elif usuarios[cedula][3] == "Administrador":

        administrador(cedula)
        
def depuracion_registros(cedula):
    print("**DEPURACION REGISTROS**")
    print("**PROFE NO NOS REBAJE MUCHO :(**")
    