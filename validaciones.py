def validar_dni(alumnos):

    dni = int(input("Ingresa el DNI del alumno: "))
    existe = True

    while existe:
        existe = False
        for dni_alumno in alumnos:
            if dni_alumno == str(dni):
                existe = True

        if existe:
            print("Ese DNI ya existe.")
            dni = int(input("Ingrese otro DNI: "))

    return dni

def validar_nombre():
    nombre = input("Ingresa el nombre del alumno: ")
    while len(nombre) == 0:
        nombre = input("El dato no puede estar vacio, ingrese el dato del alumno: ")
    return nombre

def validar_apellido():
    apellido = input("Ingresa el apellido del alumno: ")
    while len(apellido) == 0:
        apellido = input("El dato no puede estar vacio, ingrese el dato del alumno: ")
    return apellido

def validar_edad():
    edad = int(input("Ingresa la edad del alumno: "))
    while edad < 0:
        edad = int(input("Error al ingresar la edad, intentelo nuevamente: "))
    return edad

def validar_nota():
    nota = int(input("Ingresa la nota del alumno: "))
    while nota <= 0 or nota >= 11:
        nota = int(input("Error, la nota debe estar entre 1 y 10: "))
    return nota