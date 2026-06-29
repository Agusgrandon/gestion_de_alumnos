from alumnos import registrar_alumno, listar_alumnos
from archivos import cargar_json

continuar = True

while continuar:
    opcion = int(input("ingresa la opcion: "))

    match opcion: 
        case 1:
            cargar_alumnos = cargar_json("alumnos.json", "alumnos")
        case 2:
            ingresar_alumno = registrar_alumno(cargar_alumnos)
        case 3:
            mostrar_alumnos = listar_alumnos(cargar_alumnos)
            print(mostrar_alumnos)
        case 7:
            continuar = False
        case _:
            print("La opcion ingresada no es correcta, intentelo nuevamente")