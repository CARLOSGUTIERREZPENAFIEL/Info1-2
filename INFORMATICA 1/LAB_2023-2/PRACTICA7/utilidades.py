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

def leer_archivo(archivo):
    leer = open(archivo, "r")
    lista_global = []
    lista_globalNotas = []
    contador = 0
    for i in leer:
        if i != "\n":
            contador += 1
            if contador == 1:
                lista_cursos = i[:-1].split(",")
                lista_global.append(lista_cursos)
            elif contador == 2:
                lista_cedulas = i[:-1].split(" ")
                lista_global.append(lista_cedulas)
            elif contador >= 3:
                lista_notas = i[:-1].split(" ")
                lista_globalNotas.append(lista_notas)
    lista_global.append(lista_globalNotas)
    return lista_global
#print(leer_archivo("database_p7.txt"))
def cargar_datos(lista):
    notas = ""
    contador = 0
    for i in lista:
        contador += 1
        if contador == 1:
            cursos = ",".join(i)
        elif contador == 2:
            cedulas = " ".join(i)
        elif contador >= 3:
            for j in i:
                notas += ", ".join(j) + "\n"
    #print(contador)
    nueva_lista = cursos+"\n"+cedulas+"\n"+notas
    texto = open("database_p7.txt", "w")
    texto.write(nueva_lista)

#cargar_datos(x)  
 

def confirmacion(YoN):
    while True :
        if YoN=='y':
            return YoN
        elif YoN=='n':
            return YoN
        else:
            YoN=input('Ingrese una opcion valida:\n').lower()
            

            
def mostrar_curso(lista):
    archivo= leer_archivo('database_p7.txt')
    #cursos_disponibles= archivo[0]
    opcion= 1
    lista_valida=[]
    for cursos in lista:
        opc= str(opcion)
        lista_valida.append(opc)
        opciones= opc + '.' + cursos
        opcion+=1
        print(opciones) 
    return lista_valida
#mostrar_curso()

def eliminar_lista(lista, eliminar):
    nueva_lista= []
    for elim in lista:
        if elim != eliminar:
            nueva_lista.append(elim)
    return nueva_lista
def eliminar_notas(lista, posicion):
    nueva_lista = []
    for elim in range(0,len(lista)):
        if elim != posicion:
            nueva_lista.append(lista[elim])
    return nueva_lista
            
def verificar_opcion(lista, opcion):
    while True:
        if  opcion not in lista:
            opcion= input('\nIngrese Una Opcion Correcta Del Curso Que Desea Eliminar:\n')
        else:
            return opcion  
            
def eliminar_curso():
    archivo= leer_archivo('database_p7.txt')
    cursos_disponibles= archivo[0]
    nueva_global = []
    print('\n'*50)
    print('--ELIMINAR CURSO--\n \n**CURSOS DISPONIBLES**\n')
    opciones_validas= mostrar_curso(cursos_disponibles)
    eliminar_cursos= input('Que Curso Desea Eliminar:\n ')
    eliminar = verificar_opcion(opciones_validas, eliminar_cursos)
    print('\n--CURSO SELECCIONADO--\n',cursos_disponibles[int(eliminar)-1],'\n')
    YoN= input('Desea eliminar este curso:\n').lower()
    confir=confirmacion(YoN)
    if confir=='y':
        curso_eliminar = int(eliminar)-1
        nlista_curso= eliminar_lista(archivo[0], archivo[0][curso_eliminar])
        notas = archivo[2]
        nueva_listan= []
        for nota in notas:
            x= eliminar_notas(nota, curso_eliminar)
            nueva_listan.append(x)
        nueva_global.append(nlista_curso)
        nueva_global.append(archivo[1])
        nueva_global.append(nueva_listan)
        #cargar_datos(nueva_global)
        
#eliminar_curso()

def notas_validas(nota):
    while True:
        if float(nota) < 0 or float(nota)>5:
            nota= input('Ingrese Una Nota En El Rango De 0 a 5:\n')
        else:
            return nota

def añadir_curso():
    archivo= leer_archivo('database_p7.txt')
    nueva_global = []
    cursos_disponibles= archivo[0]
    notas= archivo[2]
    estudiantes= archivo[1]
    print('\n'*50)
    print('--AÑADIR CURSO--\n')
    nuevo_curso= input('Ingrese El Nombre Del Nuevo Curso:\n')
    cursos_disponibles.append(nuevo_curso)
    print('\n**AGREGAR NOTAS**\n')
    nnota=0
    for estudiante in estudiantes:
        print('\n**ESTUDIANTE ACTUAL**\n', estudiante)
        nueva_nota= input('\nIngrese La Nota De Este Estudiante:\n')
        nota=notas_validas(float(nueva_nota))
        notas[nnota].append(nota)
        nnota+=1
    
    nueva_global.append(cursos_disponibles)
    nueva_global.append(archivo[1])
    nueva_global.append(notas)
    #cargar_datos(nueva_global)
    print(nueva_global)
#añadir_curso()   

def eliminar_notas(lista, eliminar):
    nueva_listan= []
    cont=0
    for nota in lista:
        if cont != int(eliminar)-1:
            nueva_listan.append(nota)
            cont+=1
        else:
            cont+=1
    return nueva_listan

def eliminarr_estudiante():
    archivo= leer_archivo('database_p7.txt')
    nueva_global = []
    notas= archivo[2]
    estudiantes= archivo[1]
    print('\n'*50)
    print('--ELIMINAR ESTUDIANTES--\n**ESTUDIANTES DISPONIBLES**\n')
    opciones_validas= mostrar_curso(estudiantes)
    eliminar_estudiante= input('\nIngrese La Opcion Del Estudiante Que Desea Eliminar:\n')
    eliminar= verificar_opcion(opciones_validas, eliminar_estudiante)
    print('\n--ESTUDIANTE SELECCIONADO--\n',estudiantes[int(eliminar)-1],'\n')
    YoN= input('Desea eliminar este Estudiante:\n').lower()
    confir=confirmacion(YoN)
    if confir== 'y':
        nlista_estudiante= eliminar_lista(archivo[1], estudiantes[int(eliminar)-1])
        notas = archivo[2]
        nlista_nota= eliminar_notas(notas, eliminar)
    nueva_global.append(archivo[0])
    nueva_global.append(nlista_estudiante)
    nueva_global.append(nlista_nota)
    #cargar_datos(nueva_global)
    
#eliminarr_estudiante()    
def validacion_documento(documento):
    digitos_validos= '1234567890'
    for num in documento:
        if num not in digitos_validos:
            return False
    if len(documento) !=10:
        return False
    return True
            

def agregar_estudiante():
    archivo= leer_archivo('database_p7.txt')
    nueva_global = []
    cursos_disponibles= archivo[0]
    notas= archivo[2]
    estudiantes= archivo[1]
    print('\n'*50)
    print('--AGREGAR ESTUDIANTE--\n')
    nuevo_estudiante = input('Ingrese La Cedula Del Nuevo Estudiante:\n')
    validar_doc= validacion_documento(nuevo_estudiante)
    while validar_doc== False:
        nuevo_estudiante= input('Ingrese Una Cedula Valida:\n')
        validar_doc= validacion_documento(nuevo_estudiante)
    estudiantes.append(nuevo_estudiante)
    print('\n**AGREGAR NOTAS**\nESTUDAINTE:',nuevo_estudiante)
    nlista_notas=[]
    for curso in cursos_disponibles:
        print('\n--',curso,'--')
        nueva_nota= input('\nIngrese La Nota De Este Curso:\n')
        nota=notas_validas(float(nueva_nota))
        nlista_notas.append(nota)
    notas.append(nlista_notas)
    nueva_global.append(archivo[0])
    nueva_global.append(estudiantes)
    nueva_global.append(notas)
    #cargar_datos(nueva_global)
    print(nueva_global)
#agregar_estudiante()
def promedio_cursos():
    archivo= leer_archivo('database_p7.txt')
    notas= archivo[2]
    cursos= archivo[0]
    lista_nueva=[]
    lista_aux= []
    posc=0 
    while posc < len(cursos):
        aux=0
        sumatoria=0 
        for nota in notas:
            num= nota[posc]
            if num != '-1' and num!= '-2':
                print(num)
                sumatoria+= float(num)
                aux+=1
        prom= sumatoria/aux
        prom = round(prom,1)
        lista_nueva.append(prom)
        posc+=1
    fila1= [''] + cursos
    fila2= ['PROMEDIO']+lista_nueva
    lista_aux.append(fila1)
    lista_aux.append(fila2)
    imprimir_tabla(lista_aux, 10)
    
    
#promedio_estudiantes()
def promedio_estudiante(lista):
    cont = 0
    promedios = []
    lista_nueva = []
    for i in lista:
        for j in i:
            if float(j) != -1  and float(j) != -2:
                lista_nueva.append(j)
        for k in lista_nueva:
            cont += float(k)
        promedio = cont/ len(lista_nueva)
        promedio = round(promedio,1)
        promedios.append(str(promedio))
        lista_nueva = []
        cont = 0
    return promedios
def mostrar_promedio():
    archivo = leer_archivo("database_p7.txt")
    lista_nueva = []
    lista_estudiantes= []
    cursos = [""]+ archivo[0]+["PROMEDIO"]
    
    lista_nueva.append(cursos)
    notas = archivo[2]
    cedulas = archivo[1]
    promedio = promedio_estudiante(notas)
    #print("--PROMEDIOS ESTUDIANTES--")
    for i in range(0, len(cedulas)):
        
        #print("**El promedio del estudiante ",cedulas[i], "Es:**\n", promedio[i])
        lista_estudiantes.append(cedulas[i])
        for j in notas[i]:
            lista_estudiantes.append(j)
        lista_estudiantes.append(promedio[i])
        lista_nueva.append(lista_estudiantes)
        lista_estudiantes = []
    #print(lista_nueva)
    imprimir_tabla(lista_nueva, 12)
        
        
        
mostrar_promedio()
def organizar_tres_mayores(numero,cedulas,notas):
    sufstart = 0
    lista_notas_curso = []
    for i in notas:
        lista_notas_curso.append(i[int(numero)-1])
    while sufstart < len(lista_notas_curso):
        minimo = sufstart
        for i in range(sufstart+1, len(lista_notas_curso)):
             
             if lista_notas_curso[i]<lista_notas_curso[minimo]:
                 minimo = i
        temp1 = lista_notas_curso[minimo]
        temp2 = cedulas[minimo]
        lista_notas_curso[minimo] = lista_notas_curso[sufstart]
        cedulas[minimo] = cedulas[sufstart]
        lista_notas_curso[sufstart] = temp1
        cedulas[sufstart] = temp2
        sufstart += 1
    ultimos3 = len(lista_notas_curso)-3
    mayores_notas = lista_notas_curso[ultimos3:]
    mayores_cedulas = cedulas[ultimos3:]
    return mayores_notas,mayores_cedulas

def tres_notas_mayores():
    archivo = leer_archivo("database_p7.txt")
    cursos = archivo[0]
    cedulas = archivo[1]
    notas = archivo[2]
    opciones_validas = []
    lista_nueva = []
    for i in range(len(cursos)):
        print(i+1,".",cursos[i])
        opciones_validas.append(str(i+1))
    while True:
        opcion_curso = input("Ingrese el curso que desea conocer las tres notas mayores: \n")
        if opcion_curso in opciones_validas:
            break
    nuevas_notas, nuevas_cedulas = organizar_tres_mayores(opcion_curso, cedulas, notas)
    lista_nueva.append(nuevas_cedulas)
    lista_nueva.append(nuevas_notas)
    imprimir_tabla(lista_nueva, 12)
    
#tres_notas_mayores()   
def find_lista(lista,buscar):
    posc=-1
    for num in lista:
        if num==buscar:
            return posc
        else:
            posc+=1
    
         
def nota_menor():
    archivo= leer_archivo('database_p7.txt')
    cursos= archivo[0]
    estudiantes = archivo[1]
    notas= archivo[2]
    lista_aux=[]
    lista_nota=[]
    lista_curso=[]
    print('\n--NOTA MENOR ESTUDIANTE--\n')
    aux= mostrar_curso(estudiantes)
    estudiante= input('\nEliga Una Opcion:\n')
    while True:
        if estudiante not in aux:
            estudiante= input('\nEliga Una Opcion Correcta:\n')
        else:
            break
    print('\n**ESTUDIANTE SELECCIONADO**\n',estudiantes[int(estudiante)-1])
    nota= notas[int(estudiante)-1]
    aux=100
    for num in nota:
        if num != '-1' and num != '-2':
            if float(num)<aux:
                aux= float(num)
    aux= str(aux)
    posc= find_lista(nota, aux)
    lista_nota.append(aux)
    cur= cursos[posc+1]
    lista_curso.append(cur)
    fila1= ['CURSO']+['NOTA']
    fila2= lista_curso + lista_nota
    lista_aux.append(fila1)
    lista_aux.append(fila2)
    imprimir_tabla(lista_aux, 10)


def ordenar_promedios_aux(promedios,cedulas):
    sufstart = 0
    while sufstart < len(promedios):
        minimo = sufstart
        for i in range(sufstart+1, len(promedios)):
             minimo = sufstart
             if float(promedios[i])<float(promedios[minimo]):
                 minimo = i
        temp1 = promedios[minimo]
        temp2 = cedulas[minimo]
        promedios[minimo] = promedios[sufstart]
        cedulas[minimo] = cedulas[sufstart]
        promedios[sufstart] = temp1
        cedulas[sufstart] = temp2
        sufstart += 1
    return cedulas, promedios
    
def ordenar_promedios_estudiantes():
    archivo = leer_archivo("database_p7.txt")
    cursos = archivo[0]
    cedulas = archivo[1]
    notas = archivo[2]
    lista_aux = []
    lista_global = []
    lista_promedios = promedio_estudiante(notas)
    cedulas, promedios = ordenar_promedios_aux(lista_promedios, cedulas)
    fila1 = ["ESTUDIANTE"]+["PROMEDIO"]
    lista_global.append(fila1)
    for i in range(len(cedulas)-1,-1,-1):
        lista_aux.append(cedulas[i])
        lista_aux.append(promedios[i])
        lista_global.append(lista_aux)
        lista_aux = []
    imprimir_tabla(lista_global, 12)
#ordenar_promedios_estudiantes()

def calcular_posicion_lista_promedios():
    archivo = leer_archivo("database_p7.txt")
    cursos = archivo[0]
    cedulas = archivo[1]
    notas = archivo[2]
    opciones_validas = []
    for i in range(len(cedulas)):
        opciones_validas.append(str(i+1))
        print(i+1,".",cedulas[i])
    while True:
        opcion_cedula = input("Seleccione una cedula: \n")
        if opcion_cedula in opciones_validas:
            break
    cedula_buscar = cedulas[int(opcion_cedula)-1]
    lista_promedios = promedio_estudiante(notas)
    cedulas_organizadas, promedios = ordenar_promedios_aux(lista_promedios, cedulas)
    posicion = 0
    for i in range(len(cedulas_organizadas)-1,-1,-1):
        posicion += 1
        if cedula_buscar == cedulas_organizadas[i]:
            print("El estudiante con cedula ",cedula_buscar, "se encuentra en la posicion: ", posicion, "de mayor a menor")
#calcular_posicion_lista_promedios()
def ordenar_estudiantes_cantidad_cursos():
    archivos = leer_archivo("database_p7.txt")
    cursos = archivos[0]
    cedulas = archivos[1]
    notas = archivos[2]
    lista_cursos = []
    contador = 0
    for i in notas:
        for j in i:
            if j != "-2" and j != "-1":
                contador += 1
        lista_cursos.append(contador)
        contador = 0
    sufstart = 0
    while sufstart < len(lista_cursos):
        minimo = sufstart
        for i in range(sufstart+1,len(lista_cursos)):
            if lista_cursos[i]<lista_cursos[minimo]:
                minimo = i
        #print(lista_cursos)
        temp1 = lista_cursos[minimo]
        temp2 = cedulas[minimo]
        lista_cursos[minimo] = lista_cursos[sufstart]
        cedulas[minimo] = cedulas[sufstart]
        lista_cursos[sufstart]= temp1
        cedulas[sufstart]= temp2
        sufstart += 1
    #print(lista_cursos)
    lista_global = []
    lista_aux = []
    fila1 = ["ESTUDIANTES"]+["CURSOS"]
    lista_global.append(fila1)
    for i in range(len(cedulas)-1,-1,-1):
        lista_aux.append(cedulas[i])
        lista_aux.append(lista_cursos[i])
        lista_global.append(lista_aux)
        lista_aux = []
    
    imprimir_tabla(lista_global, 12)
#ordenar_estudiantes_cantidad_cursos()     

def ordenar_cancelaciones():
    archivos = leer_archivo("database_p7.txt")
    cursos = archivos[0]
    cedulas = archivos[1]
    notas = archivos[2]
    lista_cursos = []
    Lista_notas_cursos = []
    contador = 0
    for i in range(len(cursos)):
        for j in notas:
            if j[i] == "-1" :
                contador += 1
        #Lista_notas_cursos.append(contador)
        lista_cursos.append(contador)
        contador = 0
    sufstart = 0
    while sufstart < len(lista_cursos):
        minimo = sufstart
        for i in range(sufstart+1,len(lista_cursos)):
            if lista_cursos[i]<lista_cursos[minimo]:
                minimo = i
        #print(lista_cursos)
        temp1 = lista_cursos[minimo]
        temp2 = cursos[minimo]
        lista_cursos[minimo] = lista_cursos[sufstart]
        cursos[minimo] = cursos[sufstart]
        lista_cursos[sufstart]= temp1
        cursos[sufstart]= temp2
        sufstart += 1
    #print(lista_cursos)
    lista_global = []
    lista_aux = []
    fila1 = ["CURSOS"]+["CANCELACIONES"]
    lista_global.append(fila1)
    for i in range(len(cursos)-1,-1,-1):
        lista_aux.append(cursos[i])
        lista_aux.append(lista_cursos[i])
        lista_global.append(lista_aux)
        lista_aux = []
    
    imprimir_tabla(lista_global, 15)
            
ordenar_cancelaciones() 
    
    
    








#x = leer_archivo("database_p7.txt")
#print(promedio_estudiantes(x))








 