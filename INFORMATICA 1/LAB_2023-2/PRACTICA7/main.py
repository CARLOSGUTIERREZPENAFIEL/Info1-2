from utilidades import*
print("profe ayudenos que ya vamos a terminar")
print("**MENU PRINCIPAL UDEA**")
print("1.Eliminar curso")
print("2.Añadir curso")
print("3.Eliminar estudiante")
print("4.Agregar estudiante")
print("5.Promedio de estudiantes")
print("6.Promedio de cursos")
print("7.Tres notas mayores")
print("8.Menor nota de estudiante")
print("9.Ordenar promedios estudiantes")
print("10.Ordenar estudiantes por cantidad de cursos")
print("11.Ordenar cursos según cancelaciones")
while True:
    opcion = input("ingresar una opcion: \n")
    if opcion == "1":
        eliminar_curso()