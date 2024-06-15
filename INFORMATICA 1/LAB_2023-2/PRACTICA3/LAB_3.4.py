palabra = input("ingrese una palabra: \n").lower()
nueva = ""
abc = "abcdefghijklmnopqrstuvwxyz"
aux = 1
while True:
    for i in range(0, len(palabra)):
        if palabra[i] == " ":
            aux = 2
            break
        elif palabra[i] not in abc:
            aux = 2
            break
    if aux == 2:
        palabra = input("ingrese una palabra valida: \n").lower()
        aux = 1
    else:
        break
num = int(input("ingrese un numero: \n"))
while True:
    if num < 0 or num >26:
        num = int(input("ingrese un numero valido: \n"))
        
    else:
        break
for i in range(0, len(palabra)):
    posicion = abc.index(palabra[i])
    if posicion + num > 25:
        posicionF = (posicion + num)-26
    else:
        posicionF = posicion + num
    nueva += abc[posicionF]
print(nueva)