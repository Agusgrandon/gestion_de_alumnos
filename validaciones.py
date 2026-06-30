def validar_dni(alumnos:dict) -> int:
    """Solicita un DNI y verifica que no se encuentre registrado.
    Si el DNI ingresado ya existe en el diccionario de alumnos,
    solicita al usuario que ingrese uno nuevo hasta que sea único.

    Args:
        alumnos (dict): Diccionario que contiene los alumnos registrados, utilizando el DNI como clave.

    Returns:
        int: valor ingresado del DNI. 
    """
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

def validar_nombre() -> str:
    """Solicita el nombre de un alumno y verifica que no esté vacío.
    Si el usuario no ingresa ningún dato, solicita nuevamente el nombre.

    Returns:
        str: Nombre del alumno validado.
    """
    nombre = input("Ingresa el nombre del alumno: ")
    while len(nombre) == 0:
        nombre = input("El dato no puede estar vacio, ingrese el dato del alumno: ")

    return nombre

def validar_apellido() -> str:
    """Solicita el apellido de un alumno y verifica que no esté vacío.
    Si el usuario no ingresa ningún dato, solicita nuevamente el apellido.

    Returns:
        str: Apellido del alumno validado.
    """
    apellido = input("Ingresa el apellido del alumno: ")
    while len(apellido) == 0:
        apellido = input("El dato no puede estar vacio, ingrese el dato del alumno: ")

    return apellido

def validar_edad() -> int:
    """ Solicita la edad de un alumno y verifica que sea un valor válido.
    Si el usuario ingresa una edad menor que cero, solicita nuevamente el dato hasta que sea válido.

    Returns:
        int: Edad del alumno validada.
    """
    edad = int(input("Ingresa la edad del alumno: "))
    while edad < 0:
        edad = int(input("Error al ingresar la edad, intentelo nuevamente: "))

    return edad

def validar_nota() -> int:
    """Solicita la nota de un alumno y verifica que se encuentre entre 1 y 10.
    Si el usuario ingresa una nota fuera del rango permitido, solicita nuevamente el dato hasta que sea válido.

    Returns:
        int: Nota del alumno validada.
    """
    nota = int(input("Ingresa la nota del alumno: "))
    while nota <= 0 or nota >= 11:
        nota = int(input("Error, la nota debe estar entre 1 y 10: "))

    return nota