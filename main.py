from alumnos import registrar_alumno, listar_alumnos, modificar_alumno, eliminar_alumno, buscar_alumno
from archivos import cargar_json
from utilidades import menu_principal
from estadisticas import mayor_nota

continuar = True
cargar_alumnos = cargar_json("alumnos.json", "alumnos")

while continuar:
    menu_principal()
    opcion = int(input("ingresa la opcion: "))

    match opcion: 
        case 1:
            ingresar_alumno = registrar_alumno(cargar_alumnos)
        case 2:
            mostrar_alumnos = listar_alumnos(cargar_alumnos)
            print(mostrar_alumnos)
        case 3:
            buscar = buscar_alumno(cargar_alumnos)
            print(buscar)
        case 4:
            modificar = modificar_alumno(cargar_alumnos)
        case 5:
            eliminar = eliminar_alumno(cargar_alumnos)
        case 6:
            mayor_nota(cargar_alumnos)
        case 7:
            continuar = False
            print("Adiós 👋")
        case _:
            print("La opcion ingresada no es correcta, intentelo nuevamente")