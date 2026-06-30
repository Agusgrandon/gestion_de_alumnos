def cantidad_de_alumnos(alumnos:dict) -> str:
    """Calcula la cantidad total de alumnos registrados.
    La función recorre el diccionario de alumnos, cuenta la cantidad de
    registros existentes y devuelve un mensaje indicando el total de alumnos.

    Args:
        alumnos (dict): Diccionario que contiene los alumnos registrados.

    Returns:
        str: Mensaje con la cantidad total de alumnos registrados.
    """
    cantidad = 0

    for dni in alumnos:
        cantidad += 1 
    
    resultado = f"La cantidad de estudiantes es {cantidad}"

    return resultado

def promedio_notas(alumnos:dict) -> str:
    """Calcula el promedio de las notas de los alumnos registrados.
    La función recorre el diccionario de alumnos, suma todas las notas y
    calcula el promedio. Si no existen alumnos registrados, devuelve un
    mensaje indicando que no hay datos para realizar el cálculo.

    Args:
        alumnos (dict): Diccionario que contiene los alumnos registrados.

    Returns:
        str: Mensaje con el promedio de las notas o un mensaje indicando que no hay alumnos cargados.
    """
    suma = 0
    cantidad = 0

    for dni in alumnos:
        suma += alumnos[dni]["nota"]
        cantidad += 1

    if cantidad > 0:
        promedio = suma / cantidad
        mensaje = f"El promedio de las notas es {promedio}"
    else:
        mensaje = f"No hay alumnos cargados."
    
    return mensaje

def mayor_nota(alumnos:dict) -> str:
    """Obtiene el alumno con la nota más alta registrada.
    La función recorre el diccionario de alumnos, compara las notas de cada
    uno y determina cuál es la mayor. Al finalizar, devuelve un mensaje con
    el nombre, apellido y la nota del alumno que obtuvo la calificación más alta.

    Args:
        alumnos (dict): Diccionario que contiene los alumnos registrados.

    Returns:
        str: Mensaje con el nombre, apellido y la nota del alumno que obtuvo la calificación más alta.
    """
    valor_maximo = 0

    for alumno, datos in alumnos.items():
        if datos["nota"] > valor_maximo:
            valor_maximo = datos["nota"]
            nombre_maximo = datos["nombre"]
            apellido_maximo = datos["apellido"]

    mensaje = f"El alumno con la nota más alta es {nombre_maximo} {apellido_maximo}, con una nota de {valor_maximo}."

    return mensaje

def cantidad_aprobados(alumnos:dict) -> str:
    """Calcula la cantidad de alumnos aprobados.
    La función recorre el diccionario de alumnos y cuenta aquellos cuya
    nota es mayor o igual a 6. Al finalizar, devuelve un mensaje con la
    cantidad total de alumnos aprobados.

    Args:
        alumnos (dict): Diccionario que contiene los alumnos registrados.

    Returns:
        str: Mensaje con la cantidad de alumnos que aprobaron.
    """
    aprobados = 0

    for dni in alumnos:
        if alumnos[dni]["nota"] >= 6:
            aprobados += 1

    mensaje = f"La cantidad de aprobados es {aprobados}"

    return mensaje

def cantidad_desaprobados(alumnos:dict) -> str:
    """Calcula la cantidad de alumnos desaprobados.
    La función recorre el diccionario de alumnos y cuenta aquellos cuya
    nota es menor a 6. Al finalizar, devuelve un mensaje con la cantidad
    total de alumnos desaprobados.

    Args:
        alumnos (dict): Diccionario que contiene los alumnos registrados.

    Returns:
        str: Mensaje con la cantidad de alumnos desaprobados.
    """
    desaprobados = 0

    for dni in alumnos:
        if alumnos[dni]["nota"] < 6:
            desaprobados += 1

    mensaje = f"La cantidad de desaprobados es {desaprobados}"

    return mensaje

def mostrar_estadistica(alumnos:dict) -> None:
    """Muestra por pantalla las estadísticas generales de los alumnos registrados.
    La función imprime un encabezado y presenta las principales estadísticas
    obtenidas a partir de los datos de los alumnos, si todavia no hay alumnos registrados,
    muestra un mensaje de que no hay datos todavia. 

    Args:
        alumnos (dict): Diccionario que contiene los alumnos registrados.
    """
    if len(alumnos) == 0:
        print("No hay alumnos todavia para mostrar 👨‍🎓")
    else:
        print("\n---- ESTADISTICAS ----")
        print(cantidad_de_alumnos(alumnos))
        print(promedio_notas(alumnos))
        print(mayor_nota(alumnos))
        print(cantidad_aprobados(alumnos))
        print(cantidad_desaprobados(alumnos))
        print("-" * 60)