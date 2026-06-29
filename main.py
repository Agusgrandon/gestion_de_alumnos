from alumnos import registrar_alumno, listar_alumnos, modificar_alumno
from archivos import cargar_json
from utilidades import menu_principal

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
            print("buscar alumno por dni")
        case 4:
            modificar = modificar_alumno(cargar_alumnos)
        case 7:
            continuar = False
        case _:
            print("La opcion ingresada no es correcta, intentelo nuevamente")