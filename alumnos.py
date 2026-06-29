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
    apellido = input("Ingresa el apellido del alumno: ")
    edad = int(input("Ingresa la edad del alumno: "))
    nota = int(input("Ingresa la nota del alumno: "))

    alumno["dni"] = dni
    alumno["nombre"] = nombre
    alumno["apellido"] = apellido
    alumno["edad"] = edad
    alumno["nota"] = nota


    lista.append(alumno)

    guardar_datos(lista)
   

registrar_alumno()