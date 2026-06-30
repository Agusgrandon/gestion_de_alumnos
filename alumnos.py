from archivos import guardar_datos
from validaciones import validar_nombre, validar_apellido, validar_edad, validar_nota, validar_dni
from utilidades import menu_buscar

def registrar_alumno(alumnos):
 
    dni = validar_dni(alumnos)
    nombre = validar_nombre()
    apellido = validar_apellido()
    edad = validar_edad()
    nota = validar_nota()

    alumnos[str(dni)] = {
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad,
    "nota": nota
    }

    guardar_datos(alumnos)
    return alumnos

def listar_alumnos(alumnos):

    if len(alumnos) == 0:
        mensaje = f"No hay alumnos todavia para listar"
    else:
        mensaje = "\n======== ALUMNOS ==========\n"
        for dni in alumnos:
            mensaje += (f"DNI: {dni}\n"
                       f"Nombre: {alumnos[dni]['nombre']}\n"
                       f"Apellido: {alumnos[dni]['apellido']}\n"
                       f"Edad: {alumnos[dni]['edad']}\n"
                       f"Nota: {alumnos[dni]['nota']}\n"
                       f"-----------------------------\n")        
    return mensaje      

def modificar_alumno(alumnos):

    ingresar_dni = input("Ingresa el DNI del alumno que necesitas modificar: ")  
    encontrado = False

    for dni in alumnos:
        
        if dni == ingresar_dni:
            encontrado = True
            print("Dato encontrado con exito!")    
            menu_buscar()
            modificar = input("Ingresa la opcion que necesitas modificar: ")

            match modificar:
                case "1":
                    nombre = validar_nombre()
                    alumnos[ingresar_dni]["nombre"] = nombre
                    print('¡Datos modificados con exito!')
                case "2":
                    apellido = validar_apellido()
                    alumnos[ingresar_dni]["apellido"] = apellido
                    print('¡Datos modificados con exito!')
                case "3":
                    edad = validar_edad()
                    alumnos[ingresar_dni]["edad"] = edad
                    print('¡Datos modificados con exito!')
                case "4":
                    nota = validar_nota()
                    alumnos[ingresar_dni]["nota"] = nota
                    print('¡Datos modificados con exito!')

    if encontrado == False:
        print(f"El DNI que ingresaste no existe en el listado de alumnos 😥")

    guardar_datos(alumnos)

    return alumnos

def buscar_alumno(alumnos):
    ingresar_dni = input("Ingresa el DNI del alumno que necesitas buscar: ")
    encontrado = False

    for dni in alumnos:
        if dni == ingresar_dni:
            encontrado = True
            mensaje = f"Dato encontrado con exito, nombre {alumnos[dni]['nombre']} {alumnos[dni]['apellido']}, edad {alumnos[dni]['edad']}, nota {alumnos[dni]['nota']}."

    if encontrado == False:
        mensaje = f"El DNI que ingresaste no existe en el listado de alumnos 😥"

    return mensaje
     
def eliminar_alumno(alumnos):

    ingresar_dni = input("Ingresa el DNI del alumno que necesitas eliminar: ")

    encontrado = False
    eliminar = False

    for dni in alumnos:

        if dni == ingresar_dni:

            encontrado = True

            print(f"Dato encontrado, la baja a realizar es del alumno: {alumnos[dni]['nombre']} {alumnos[dni]['apellido']}")

            baja = input("¿Querés darlo de baja? (Si/No): ")

            match baja:

                case "SI" | "Si" | "si":
                    eliminar = True

                case "NO" | "No" | "no":
                    print("El alumno no se dio de baja")

                case _:
                    print("No entendí la respuesta, intentalo nuevamente 👩‍💻")

    if encontrado == False:
        print("El DNI que ingresaste no existe 😥")

    elif eliminar == True:
        alumnos.pop(ingresar_dni)
        print("Alumno dado de baja")

    guardar_datos(alumnos)

    return alumnos
