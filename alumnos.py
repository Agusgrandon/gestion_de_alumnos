from archivos import guardar_datos
from validaciones import validar_nombre, validar_apellido, validar_edad, validar_nota, validar_dni
from utilidades import menu_buscar

def registrar_alumno(alumnos:dict) -> dict:
    """Registra un nuevo alumno en el sistema.
    Solicita y valida el DNI, nombre, apellido, edad y nota del alumno.
    Luego almacena la información en el diccionario de alumnos y guarda los cambios en el archivo JSON.

    Args:
        alumnos (dict): Diccionario que contiene los alumnos registrados.

    Returns:
        dict: Diccionario de alumnos actualizado con el nuevo registro.
    """
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

def listar_alumnos(alumnos:dict) -> str:
    """Genera un listado de todos los alumnos registrados.
    La función recorre el diccionario de alumnos y construye un mensaje en formato
    de texto con la información de cada alumno (DNI, nombre, apellido, edad y nota).
    Si no hay alumnos cargados, devuelve un mensaje indicando que la lista está vacía.

    Args:
        alumnos (dict): Diccionario que contiene los alumnos registrados.

    Returns:
        str: Cadena de texto con el listado completo de alumnos o un mensaje indicando que no hay alumnos registrados.
    """
    if len(alumnos) == 0:
        mensaje = f"No hay alumnos todavia para mostrar"
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

def modificar_alumno(alumnos:dict) -> dict:
    """Permite modificar los datos de un alumno existente en el sistema.
    La función solicita el DNI del alumno a modificar, lo busca dentro del
    diccionario y, si lo encuentra, permite seleccionar qué campo actualizar
    (nombre, apellido, edad o nota). Luego de la modificación, guarda los cambios.

    Args:
        alumnos (dict): Diccionario que contiene los alumnos registrados.

    Returns:
        dict: Diccionario actualizado con los datos modificados.
    """

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

def buscar_alumno(alumnos:dict) -> str:
    """Busca un alumno dentro del diccionario a partir de su DNI y devuelve sus datos.

    Args:
        alumnos (dict): Diccionario que contiene los alumnos registrados.

    Returns:
        str: Mensaje con los datos del alumno encontrado o un mensaje de error si el DNI no existe.
    """
    ingresar_dni = input("Ingresa el DNI del alumno que necesitas buscar: ")
    encontrado = False

    for dni in alumnos:
        if dni == ingresar_dni:
            encontrado = True
            mensaje = f"Dato encontrado con exito, nombre {alumnos[dni]['nombre']} {alumnos[dni]['apellido']}, edad {alumnos[dni]['edad']}, nota {alumnos[dni]['nota']}."

    if encontrado == False:
        mensaje = f"El DNI que ingresaste no existe en el listado de alumnos 😥"

    return mensaje
     
def eliminar_alumno(alumnos:dict) -> dict:
    """Permite eliminar un alumno del sistema a partir de su DNI.
    La función solicita el DNI del alumno, verifica si existe en el diccionario
    y, en caso afirmativo, muestra sus datos para confirmar la eliminación.
    Luego solicita confirmación al usuario para dar de baja al alumno.
    Si se confirma, elimina el registro del diccionario y guarda los cambios.

    Args:
        alumnos (dict): Diccionario que contiene los alumnos registrados.

    Returns:
        dict: Diccionario actualizado. 
    """

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
