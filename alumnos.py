from archivos import guardar_datos
from utilidades import menu_buscar

def registrar_alumno(lista):
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
    while edad < 0:
     edad = int(input("Error al ingresar la edad, intentelo nuevamente: "))

    nota = int(input("Ingresa la nota del alumno: "))
    while nota <= 0 or nota >= 11:
        nota = int(input("Error, la nota debe estar entre 1 y 10: "))

    alumno["dni"] = dni
    alumno["nombre"] = nombre
    alumno["apellido"] = apellido
    alumno["edad"] = edad
    alumno["nota"] = nota


    lista.append(alumno)
    guardar_datos(lista)
    return lista 



def listar_alumnos(lista):

    if len(lista) == 0:
        mensaje = f"No hay alumnos todavia para listar"
    else:
        mensaje = ""
        for alumnos in lista:
            mensaje += (f"DNI: {alumnos['dni']}.\n"
                       f"Nombre: {alumnos['nombre']}.\n"
                       f"Apellido: {alumnos['apellido']}.\n"
                       f"Edad: {alumnos['edad']}.\n"
                       f"Nota: {alumnos['nota']}.\n"
                       f"-----------------------------\n")
    return mensaje      

def modificar_alumno(lista):

    ingresar_dni = int(input("Ingresa el DNI del alumno que necesitas modificar: "))    

    for alumno in lista:
        if alumno['dni'] == ingresar_dni:
            print("Dato encontrado con exito!")    
            menu_buscar()
            modificar = input("Ingresa la opcion que necesitas modificar: ")

            match modificar:
                case "1":
                    nombre = input("Ingresa el nombre del alumno: ")
                    while len(nombre) == 0:
                        nombre = input("El dato no puede estar vacio, ingrese el nombre del alumno: ")
                    alumno["nombre"] = nombre
                    print('¡Datos modificados con exito!')
                case "2":
                    apellido = input("Ingresa el apellido del alumno: ")
                    while len(apellido) == 0:
                        nombre = input("El dato no puede estar vacio, ingrese el apellido del alumno: ")
                    alumno["apellido"] = apellido
                    print('¡Datos modificados con exito!')
                case "3":
                    edad = int(input("Ingresa la edad del alumno: "))
                    while edad < 0:
                        edad = int(input("Error al ingresar la edad, intentelo nuevamente: "))
                    alumno["edad"] = edad
                    print('¡Datos modificados con exito!')
                case "4":
                    nota = int(input("Ingresa la nota del alumno: "))
                    while nota <= 0 or nota >= 11:
                        nota = int(input("Error, la nota debe estar entre 1 y 10: "))
                    alumno["nota"] = nota
                    print('¡Datos modificados con exito!')
    return lista
