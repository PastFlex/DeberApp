# Sistema de Gestión de Estudiantes y Notas

Proyecto académico desarrollado en **Python 3** ejecutado exclusivamente por consola/terminal, diseñado para demostrar conceptos fundamentales de lógica y algoritmia estructurada.

---

## 📌 Descripción del Proyecto
El **Sistema de Gestión de Estudiantes y Notas** es una aplicación interactiva que permite a un docente o administrador escolar gestionar alumnos y sus calificaciones académicas. El software opera en la terminal mediante un menú numérico continuo, garantizando la validación rigurosa de cada dato ingresado y automatizando el cálculo de promedios, la condición de aprobación o reprobación, y la generación de estadísticas del curso.

---

## 🎯 Objetivo
Desarrollar una solución algorítmica completa, clara y estructurada utilizando únicamente los fundamentos de programación procedural en Python (funciones, listas, diccionarios, condicionales y bucles), sin interfaces gráficas, frameworks ni librerías externas.

---

## 🚀 Funcionalidades Principales
1. **Registrar estudiante:** Permite ingresar alumnos con validación de nombre no vacío y prevención de duplicados.
2. **Ingresar notas:** Registra múltiples notas por estudiante en una escala de **0.0 a 10.0**, validando tipo numérico y rango permitido.
3. **Mostrar todos los estudiantes:** Lista tabular ordenada con índice, nombre, notas y promedio individual.
4. **Buscar un estudiante por nombre:** Búsqueda lineal insensible a mayúsculas/minúsculas.
5. **Calcular y mostrar promedio:** Cálculo aritmético exacto de las calificaciones del estudiante.
6. **Determinar estado de aprobación:** 
   - **Aprobado:** Promedio $\ge 7.0$
   - **Reprobado:** Promedio $< 7.0$
7. **Mostrar resumen general:** Reporte con total de estudiantes, evaluados, aprobados, reprobados, promedio general del grupo, y el estudiante con el rendimiento más alto y más bajo.
8. **Salir del programa:** Cierre seguro y controlado del menú interactivo.

---

## 💻 Requisitos
- **Python 3.8** o superior instalado en el sistema.
- Cualquier terminal o consola de comandos (PowerShell, CMD, Bash, terminal integrada de Visual Studio Code).

---

## ⚙️ Cómo Ejecutar el Programa
1. Abre tu terminal o consola de comandos.
2. Dirígete a la carpeta raíz del proyecto:
   ```bash
   cd "ruta/del/proyecto"
   ```
3. Ejecuta el archivo principal con Python:
   ```bash
   python main.py
   ```

---

## 🧠 Estructuras de Programación Utilizadas

### 1. Estructuras Condicionales (`if`, `elif`, `else`)
- **Control de menú:** Se utiliza una cadena `if / elif / else` para comparar la opción ingresada por el usuario (del `"1"` al `"8"`) y ejecutar la función correspondiente. La rama `else` atrapa cualquier entrada no válida sin cerrar el programa.
- **Regla de aprobación:** Se evalúa si `promedio >= 7.0` para dictaminar `"APROBADO"`, o por `else` clasificar como `"REPROBADO"`.
- **Validaciones lógicas:** Se evalúa si una cadena está vacía (`not nombre`), si un estudiante ya existe, o si una nota se encuentra fuera del intervalo $[0.0, 10.0]$.

### 2. Estructuras Repetitivas (`while`, `for`)
- **Bucle `while`:** 
  - Mantiene el menú activo (`while True:`) hasta que el usuario decida salir explícitamente con la opción `8`.
  - Repite la solicitud de entrada de nombres y notas hasta que el usuario ingrese datos correctos.
- **Bucle `for`:**
  - Recorre la lista de estudiantes para búsquedas lineales y reportes tabulares.
  - Itera sobre la lista de notas de cada estudiante para sumar los valores (`suma += nota`) y calcular promedios.
  - Recorre los estudiantes evaluados para determinar los valores máximos y mínimos del grupo.

### 3. Funciones (`def`)
- El programa está dividido en funciones pequeñas y modulares, donde cada una cumple una tarea específica (`mostrarMenu`, `registrarEstudiante`, `ingresarNotas`, `calcularPromedio`, `determinarEstado`, etc.).
- Facilita la reutilización de código y la legibilidad.

### 4. Listas (`[]`)
- Se utiliza la lista global `estudiantes = []` como contenedor dinámico en memoria.
- Cada estudiante almacena su propia lista de notas numéricas: `[8.5, 9.0, 7.0]`.

### 5. Diccionarios (`{}`)
- Cada estudiante es representado como un diccionario clave-valor:
  ```python
  {
      "nombre": "Ana Gomez",
      "notas": [8.5, 9.0]
  }
  ```
- Permite acceder a los datos de forma clara y semántica: `estudiante["nombre"]` y `estudiante["notas"]`.

---

## 📋 Ejemplo de Funcionamiento en Consola

```text
==================================================
      SISTEMA DE GESTIÓN DE ESTUDIANTES Y NOTAS
==================================================
1. Registrar estudiante
2. Ingresar notas de un estudiante
3. Mostrar todos los estudiantes registrados
4. Buscar un estudiante por nombre
5. Calcular y mostrar promedio de un estudiante
6. Mostrar si el estudiante está aprobado o reprobado
7. Mostrar resumen general del curso
8. Salir del programa
==================================================
Seleccione una opción (1-8): 1

--- REGISTRAR ESTUDIANTE ---
Ingrese el nombre completo del estudiante (o 'c' para cancelar): Ana Gomez
Éxito: El estudiante 'Ana Gomez' fue registrado correctamente.
```

---

## 📁 Estructura del Proyecto

```text
sistema-notas/
│
├── main.py                     # Archivo principal con todo el código ejecutable
├── README.md                   # Documentación general del repositorio
│
├── diagramas/
│   └── README.md               # 5 Diagramas de flujo en formato Mermaid
│
└── docs/
    ├── explicacion_proyecto.md  # Documento formal teórico (Paso 1 del deber)
    └── guiones_videos.md       # Guiones detallados para videos (Paso 1, 2 y Demo)
```

---

## 👤 Autor
Proyecto realizado para la asignatura de **Lógica de Programación**.
