from alumnos import registrar_alumno, listar_alumnos, modificar_alumno, eliminar_alumno, buscar_alumno
from archivos import cargar_json
from utilidades import menu_principal, titulo_del_programa
from estadisticas import mostrar_estadistica

continuar = True
cargar_alumnos = cargar_json("alumnos.json", "alumnos")
titulo_del_programa()

while continuar:
    menu_principal()
    opcion = int(input("ingresa la opcion: "))

    match opcion: 
        case 1:
            registrar_alumno(cargar_alumnos)
        case 2:
            mostrar_alumnos = listar_alumnos(cargar_alumnos)
            print(mostrar_alumnos)
        case 3:
            buscar = buscar_alumno(cargar_alumnos)
            print(buscar)
        case 4:
            modificar_alumno(cargar_alumnos)
        case 5:
            eliminar_alumno(cargar_alumnos)
        case 6:
            mostrar_estadistica(cargar_alumnos)
        case 7:
            continuar = False
            print("Adiós 👋")
        case _:
            print("La opcion ingresada no es correcta, intentelo nuevamente")