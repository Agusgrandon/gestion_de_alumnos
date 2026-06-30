def cantidad_de_alumnos(alumnos):
    cantidad = 0

    for dni in alumnos:
        cantidad += 1 
    
    resultado = f"La cantidad de estudiantes es {cantidad}"

    return resultado

def promedio_notas(alumnos):
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

def mayor_nota(alumnos):

    valor_maximo = 0

    for alumno, datos in alumnos.items():

        if datos["nota"] > valor_maximo:
            valor_maximo = datos["nota"]
            nombre_maximo = datos["nombre"]
            apellido_maximo = datos["apellido"]

    mensaje = (f"El alumno con mayor nota es "
               f"{nombre_maximo} {apellido_maximo}, "
               f"con una nota de {valor_maximo}.")

    return mensaje

def cantidad_aprobados(alumnos):
    aprobados = 0

    for dni in alumnos:
        if alumnos[dni]["nota"] >= 6:
            aprobados += 1

    mensaje = f"La cantidad de aprobados es {aprobados}"

    return mensaje

def cantidad_desaprobados(alumnos):
    desaprobados = 0

    for dni in alumnos:
        if alumnos[dni]["nota"] < 6:
            desaprobados += 1

    mensaje = f"La cantidad de desaprobados es {desaprobados}"

    return mensaje

def mostrar_estadistica(alumnos):
    print("\n---- ESTADISTICAS ----")
    print(cantidad_de_alumnos(alumnos))
    print(promedio_notas(alumnos))
    print(mayor_nota(alumnos))
    print(cantidad_aprobados(alumnos))
    print(cantidad_desaprobados(alumnos))
    print("-" * 60)