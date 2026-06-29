"""6. Estadísticas 

Implementar funciones que informen: 

Cantidad total de alumnos.  

Promedio de notas.  

Alumno con mayor nota.  

Cantidad de aprobados (≥ 6).  

Cantidad de desaprobados (< 6).  

7. Persistencia """
def mayor_nota(lista):
    mayor = 10
    for alumno, nota in lista.items():
        if nota > mayor:
            mayor = nota
            nombre = alumno

    print("el alumno con mayor nota es {nombre}")