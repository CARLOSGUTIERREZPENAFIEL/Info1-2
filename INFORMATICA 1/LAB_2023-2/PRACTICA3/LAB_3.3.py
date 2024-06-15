
palabra = input("ingrese una palabra: \n").lower()
abc = "abcdefghijklmnopqrstuvwxyz"
aux=""

    
while True:
    if " " in palabra:
        palabra = input("ingrese una sola palabra valida: \n")
    else:
            break
for i in range(len(palabra)-1,-1,-1):
    if palabra[i] not in  abc:
        palabra = input("ingrese una palabra valida: \n")
        break
    else:
        aux += palabra[i]
if palabra == aux:
    print("ES PALINDROMA")
        
else:
    print("NO ES PALINDROMA")
        
        
    
