# 🎓 Sistema de Gestión de Alumnos

Proyecto desarrollado en **Python** para administrar la información de alumnos utilizando funciones, modularización, validaciones y persistencia de datos mediante archivos JSON.

---

# 📌 Descripción

Este programa permite gestionar un registro de alumnos de una institución educativa mediante un menú interactivo.

Cada alumno posee la siguiente información:

- DNI
- Nombre
- Apellido
- Edad
- Nota final

El sistema almacena toda la información en un archivo **JSON**, permitiendo conservar los datos entre distintas ejecuciones del programa.

---

# 🛠 Tecnologías utilizadas

- Python 3
- JSON (persistencia de datos)

---

# 📂 Estructura del proyecto

```bash
📦 ALUMNOS_PROGRAMACION
 ┣ 📂 data
 ┃ ┗ 📜 alumnos.json
 ┣ 📜 alumnos.py
 ┣ 📜 archivos.py
 ┣ 📜 estadisticas.py
 ┣ 📜 main.py
 ┣ 📜 menu.py
 ┣ 📜 utilidades.py
 ┣ 📜 validaciones.py
 ┗ 📜 README.md
```

### Organización de los módulos

- **main.py:** Punto de entrada del programa. Inicia la ejecución del sistema.
- **alumnos.py:** Contiene las funciones relacionadas con la gestión de alumnos (registro, listado, búsqueda, modificación y eliminación).
- **archivos.py:** Administra la lectura y escritura del archivo `alumnos.json`.
- **estadisticas.py:** Contiene las funciones encargadas de generar las estadísticas del sistema.
- **menu.py:** Muestra el menú interactivo y permite acceder a las distintas funcionalidades del programa.
- **utilidades.py:** Reúne funciones de apoyo encargadas de mostrar los menús y mensajes utilizados durante la ejecución del programa.
- **validaciones.py:** Implementa las funciones de validación de los datos ingresados por el usuario.
- **data/alumnos.json:** Archivo donde se almacenan de forma permanente los datos de los alumnos.

---

# ⚙️ Funcionalidades

## 1️⃣ Registrar alumno

Permite registrar un nuevo alumno en el sistema.

Validaciones implementadas:

- No se permiten DNI duplicados.
- La edad no puede ser negativa.
- La nota debe estar comprendida entre 0 y 10.
- Se validan todos los datos antes de ser almacenados.

---

## 2️⃣ Listar alumnos

Muestra todos los alumnos registrados con la siguiente información:

- DNI
- Nombre
- Apellido
- Edad
- Nota final

---

## 3️⃣ Buscar alumno

Permite buscar un alumno mediante su DNI y visualizar toda su información.

---

## 4️⃣ Modificar alumno

Permite modificar los datos de un alumno existente.

Los campos que pueden modificarse son:

- Nombre
- Apellido
- Edad
- Nota final

Los cambios realizados se guardan automáticamente.

---

## 5️⃣ Eliminar alumno

Permite eliminar un alumno utilizando su DNI.

Antes de realizar la eliminación, el sistema solicita una confirmación para evitar bajas accidentales.

---

## 6️⃣ Estadísticas

El sistema genera las siguientes estadísticas:

- Cantidad total de alumnos.
- Promedio de notas.
- Alumno con la mayor nota.
- Cantidad de alumnos aprobados (nota mayor o igual a 6).
- Cantidad de alumnos desaprobados (nota menor a 6).

---

## 7️⃣ Persistencia de datos

Toda modificación realizada sobre los alumnos se almacena automáticamente en el archivo:

```text
data/alumnos.json
```

De esta manera, la información permanece disponible incluso después de cerrar el programa.

---

## 8️⃣ Menú interactivo

El sistema funciona mediante un menú de opciones que permite acceder de manera sencilla a todas las funcionalidades disponibles.

---

# 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/Agusgrandon/gestion_alumnos.git
```

2. Ejecutar el archivo principal:

```bash
python main.py
```

---


# ✨ Autor

Proyecto desarrollado por **Agus Grandon** 💻