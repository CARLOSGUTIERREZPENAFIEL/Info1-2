palabra = input("ingresar una palabra o frase: \n").lower()
letra = input("ingresar letra: \n").lower()
aux = ""
aux2 = 1
abc = "abcdefghijklmnopqrstuvwxyz "
while True:
    for i in palabra:
        if i not in abc:
            aux2 = 2 
    if aux2 != 1:
        palabra = input("ingresar una palabra o frase valida: \n").lower()
        aux2 = 1
    elif letra not in abc or len(letra)!= 1:
        letra = input("ingresar letra valida: \n").lower()
    else:
        break
for i in range(0, len(palabra)):
    if palabra[i] == letra:
        aux += "*"
    else:
        aux += palabra[i]
print(aux)
        