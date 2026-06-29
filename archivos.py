import json

def cargar_json(nombre_archivo, key):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    return(data[key])

def guardar_datos(alumnos):
    with open("alumnos.json", "w", encoding="utf-8") as archivo:
        json.dump({"alumnos": alumnos}, archivo, indent=4)



