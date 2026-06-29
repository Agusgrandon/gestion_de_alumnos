import json

def cargar_archivo():

    with open("alumnos.json", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    lista_alumnos = json.loads(contenido)

    return lista_alumnos

def guardar_datos(lista_alumnos):

    with open("alumnos.json", "w", encoding="utf-8") as archivo:
        json.dump(lista_alumnos, archivo, indent=4)