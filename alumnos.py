from archivos import cargar_archivo, guardar_datos

def registrar_alumno():
    lista = cargar_archivo()

    alumno = {}

    dni = int(input("Ingresa el DNI: "))
    nombre = input("Agrega el nombre")
    apellido = input("Ingresa el apellido: ")

    alumno["dni"] = dni
    alumno["nombre"] = nombre
    alumno["apellido"] = apellido

    lista.append(alumno)

    guardar_datos(lista)
    print("alumno ok")

registrar_alumno()