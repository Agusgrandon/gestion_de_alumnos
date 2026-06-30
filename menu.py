from alumnos import registrar_alumno, listar_alumnos, modificar_alumno, eliminar_alumno, buscar_alumno
from archivos import cargar_json
from estadisticas import mostrar_estadistica
from utilidades import titulo_del_programa, opciones_de_menu

def ejecucion_menu_principal() -> None:
    """Ejecuta el menú principal del sistema de gestión de alumnos.
    La función carga los datos almacenados en el archivo JSON, muestra el
    título del programa y mantiene un menú interactivo que permite al usuario
    realizar las distintas operaciones disponibles sobre los alumnos
    registrados.
    """
    continuar = True
    cargar_alumnos = cargar_json("data/alumnos.json", "alumnos")
    titulo_del_programa()

    while continuar:

        opciones_de_menu()
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