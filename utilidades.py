def titulo_del_programa() -> None:
    """Muestra el título principal del programa. 
    """
    print("\n======== Sistema de Gestión de Alumnos ==========\n")

def opciones_de_menu() -> None:
    """Muestra las opciones del menu principal. 
    """
    print("1) Registrar alumno")
    print("2) Listar alumnos")
    print("3) Buscar alumno")
    print("4) Modificar alumno")
    print("5) Eliminar alumno")
    print("6) Ver estadisticas")
    print("7) Salir\n")

def menu_buscar() -> None:
    """Muestra las opciones disponibles para modificar los datos de un alumno.
    """
    print("1) Nombre")
    print("2) Apellido")
    print("3) Edad")
    print("4) Nota")
