from archivos import cargar_archivo, guardar_datos

def registrar_alumno():
    lista = cargar_archivo()

    alumno = {}

    dni = int(input("Ingresa el DNI del alumno: "))
    existe_dni = False
    for alumnos in lista:
        if alumnos["dni"] == dni:
            existe_dni = True
    while existe_dni == True:
        dni = int(input("Ese DNI ya existe, reingrese el DNI: "))
        existe_dni = False
        for alumnos in lista:
            if alumnos["dni"] == dni:
                existe_dni = True

    nombre = input("Ingresa el nombre del alumno: ")
    while len(nombre) == 0:
        nombre = input("El dato no puede estar vacio, ingrese el nombre del alumno: ")

    apellido = input("Ingresa el apellido del alumno: ")
    while len(apellido) == 0:
        apellido = input("El dato no puede estar vacio, ingrese el apellido del alumno: ")

    edad = int(input("Ingresa la edad del alumno: "))
    while edad <= 0:
     edad = int(input("Error al ingresar la edad, intentelo nuevamente: "))

    nota = int(input("Ingresa la nota del alumno: "))
    while nota <= 0 or nota >= 10:
        nota = int(input("Error, la nota debe estar entre 1 y 10: "))

    alumno["dni"] = dni
    alumno["nombre"] = nombre
    alumno["apellido"] = apellido
    alumno["edad"] = edad
    alumno["nota"] = nota


    lista.append(alumno)

    guardar_datos(lista)
   

registrar_alumno()