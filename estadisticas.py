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

def mayor_nota(alumnos):

    valor_maximo = 0

    for alumno, datos in alumnos.items():

        if datos["nota"] > valor_maximo:
            valor_maximo = datos["nota"]
            alumno_maximo = alumno

    print(alumno_maximo)

def cantidad_aprobados(alumnos):
    aprobados = 0

    for dni in alumnos:
        if alumnos[dni]["nota"] >= 6:
            aprobados += 1

    mensaje = f"La cantidad de aprobados es {aprobados}"

    return mensaje