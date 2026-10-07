# Documentación del Proyecto: Sistema de Gestión de Estudiantes y Notas

**Asignatura:** Lógica de Programación / Fundamentos de Programación  
**Proyecto:** Sistema de Gestión de Estudiantes y Notas en Consola  
**Lenguaje de Desarrollo:** Python 3  
**Entorno de Desarrollo Integrado (IDE):** Visual Studio Code (VS Code)  

---

## 1. Problema que se desea resolver
En los entornos académicos y de aula, el control de listas de alumnos, el registro manual de calificaciones y el cálculo individual de promedios suelen realizarse mediante cuadernos de apuntes o cálculos manuales propensos a errores humanos (tales como errores de suma, omisión de datos o calificaciones fuera de la escala reglamentaria).

Asimismo, determinar de manera manual e inmediata si un estudiante aprueba o reprueba, o consolidar un informe general del desempeño del grupo (promedio grupal, estudiante con mayor y menor calificación, cantidad de aprobados y reprobados) demanda tiempo considerable. 

Este proyecto resuelve dicha necesidad mediante una herramienta digital automatizada, liviana y eficiente que se ejecuta directamente en la terminal, garantizando integridad de datos y cálculo exacto.

---

## 2. Justificación de la elección del proyecto
Se eligió este proyecto porque representa un modelo ideal para aplicar de forma integral los conceptos fundamentales de la lógica de programación:

1. **Aplicabilidad práctica inmediata:** Modela un caso de uso real comprensible para cualquier estudiante o docente.
2. **Dominio de estructuras esenciales:** Permite combinar armoniosamente colecciones dinámicas (listas y diccionarios), control de flujo interactivo (bucles `while` y `for`), toma de decisiones (`if`, `elif`, `else`) y modularidad mediante funciones.
3. **Énfasis en la calidad de software básico:** Fomenta la validación estricta de datos de entrada (evitar nombres vacíos, evitar duplicados, controlar rangos de 0.0 a 10.0 y manejar errores de tipo de dato).
4. **Claridad conceptual:** Al prescindir deliberadamente de interfaces gráficas o bases de datos pesadas, el foco de evaluación se mantiene 100% sobre la lógica algorítmica y la resolución de problemas.

---

## 3. Objetivos del Proyecto

### 3.1 Objetivo General
Desarrollar un sistema de software por consola en lenguaje Python para la administración de estudiantes y calificaciones académicas, aplicando principios de lógica estructurada, funciones modulares, estructuras repetitivas, condicionales y colecciones de datos, asegurando la consistencia en el cálculo de promedios y estados de aprobación.

### 3.2 Objetivos Específicos
1. **Diseñar e implementar estructuras de almacenamiento dinámicas en memoria:** Utilizar una lista de diccionarios para representar eficientemente a cada estudiante con su nombre y su colección de notas.
2. **Implementar algoritmos de validación y control de errores:** Asegurar que el sistema no colapse ante entradas inválidas, impidiendo nombres vacíos, nombres duplicados y calificaciones fuera del rango reglamentario de 0.0 a 10.0.
3. **Automatizar el procesamiento cuantitativo de notas:** Programar funciones que calculen promedios aritméticos exactos, clasifiquen el estado del alumno (Aprobado con nota $\ge 7.0$ y Reprobado con nota $< 7.0$) y generen estadísticas consolidadas del grupo de estudiantes.
4. **Construir una interfaz de usuario por consola intuitiva y robusta:** Facilitar la interacción mediante un menú numérico interactivo controlado por un bucle continuo que guíe al usuario paso a paso.

---

## 4. Funcionalidades Identificadas del Sistema
El sistema cuenta con 8 opciones principales:
1. **Registrar estudiante:** Permite ingresar nuevos alumnos garantizando nombres únicos y no vacíos.
2. **Ingresar notas de un estudiante:** Permite añadir múltiples calificaciones a un alumno existente, validando formato decimal y rango (0.0 a 10.0).
3. **Mostrar todos los estudiantes registrados:** Presenta una tabla organizada con el número de lista, nombre, notas y promedio individual.
4. **Buscar un estudiante por nombre:** Búsqueda lineal insensible a mayúsculas/minúsculas con despliegue de ficha completa.
5. **Calcular y mostrar promedio de un estudiante:** Cálculo matemático específico sobre las calificaciones del alumno.
6. **Mostrar estado de aprobación (Aprobado/Reprobado):** Dictamina el resultado académico con base en la regla de corte (7.0).
7. **Mostrar resumen general del curso:** Muestra métricas globales (total de alumnos, aprobados, reprobados, promedio general del curso, mejor promedio y menor promedio).
8. **Salir del programa:** Cierre seguro y controlado de la sesión.

---

## 5. Modelo Entrada - Proceso - Salida (I-P-O)

```
+-------------------------------------------------------------------------------+
|                             ENTRADAS (Inputs)                                 |
| - Opción numérica seleccionada del menú (1 a 8).                              |
| - Nombre completo del estudiante (cadena de texto).                           |
| - Cantidad de notas a ingresar (número entero positivo).                      |
| - Calificaciones del estudiante (números de punto flotante entre 0.0 y 10.0). |
+-------------------------------------------------------------------------------+
                                      |
                                      v
+-------------------------------------------------------------------------------+
|                             PROCESOS (Process)                                |
| 1. Bucle interactivo while que mantiene activo el menú.                       |
| 2. Validación de cadenas vacías con .strip() y búsqueda previa de duplicados.  |
| 3. Búsqueda lineal con bucle for comparando nombres normalizados con .lower().|
| 4. Validación de rango (0.0 <= nota <= 10.0) y manejo de excepciones float.  |
| 5. Acumulación de notas mediante bucle for: suma += nota.                     |
| 6. Cálculo de promedio aritmético: promedio = suma / len(notas).              |
| 7. Decisión condicional con if / else:                                        |
|       Si promedio >= 7.0 -> "APROBADO", de lo contrario -> "REPROBADO".       |
| 8. Búsqueda de mínimos y máximos mediante comparaciones condicionales.        |
+-------------------------------------------------------------------------------+
                                      |
                                      v
+-------------------------------------------------------------------------------+
|                              SALIDAS (Outputs)                                |
| - Menú visual de consola formateado.                                          |
| - Mensajes informativos de éxito, confirmación o advertencia de error.        |
| - Listado tabular de estudiantes con nombres, notas y promedios.              |
| - Reporte individual del estudiante (notas, promedio y estado).               |
| - Resumen estadístico global del curso.                                       |
| - Mensaje formal de cierre de programa.                                       |
+-------------------------------------------------------------------------------+
```

---

## 6. Explicación de la Lógica Empleada
La arquitectura del programa se basa en el **paradigma estructurado y modular**:

- **Almacenamiento Centralizado:** Se define una lista global `estudiantes = []`. Cada elemento de esta lista es un diccionario de Python:
  ```python
  {
      "nombre": "Ana Gómez",
      "notas": [8.5, 9.0, 7.5]
  }
  ```
- **Modularidad:** El código divide cada tarea en funciones con una única responsabilidad (`mostrarMenu`, `buscarEstudiante`, `calcularPromedio`, `determinarEstado`, etc.).
- **Flujo Cíclico Principal:** La función `main()` contiene un bucle `while True:` que solo se detiene cuando el usuario selecciona explícitamente la opción `8`.
- **Validaciones Preventivas:** Cada vez que el usuario ingresa datos, se evalúan las condiciones antes de almacenar la información, protegiendo al sistema de estados inconsistentes.

---

## 7. Justificación Tecnológica

### 7.1 ¿Por qué se eligió Python?
1. **Sintaxis limpia y legible:** Python utiliza sangría obligatoria y palabras clave en inglés muy intuitivas, lo que reduce la carga sintáctica y permite enfocarse de lleno en la lógica de programación.
2. **Estructuras de datos nativas de alto nivel:** Incorpora de fábrica listas dinámicas y diccionarios asociativos sin requerir punteros ni gestión manual de memoria.
3. **Manejo sencillo de tipos y conversión de datos:** La conversión de cadenas a tipos numéricos (`int`, `float`) y el manejo de excepciones (`try / except`) es directo y robusto.
4. **Portabilidad absoluta:** El mismo código se ejecuta de manera idéntica en Windows, macOS o Linux sin modificaciones.

### 7.2 ¿Por qué se eligió Visual Studio Code (VS Code)?
1. **Entorno liviano y potente:** Es un editor de código fuente moderno, rápido y altamente configurable.
2. **Terminal integrada:** Permite escribir código en la parte superior y ejecutarlo en la consola inferior en la misma pantalla, ideal para proyectos por terminal.
3. **Integración nativa con Git y GitHub:** Facilita el control de versiones, creación de ramas, commits y sincronización con repositorios remotos.
4. **Depuración paso a paso (Debugging):** Permite colocar puntos de interrupción (*breakpoints*) para observar cómo cambian las variables en cada iteración del bucle.

---

## 8. Estructuras Lógicas Utilizadas en el Código

| Estructura | Ejemplo en el Código | Justificación de Uso |
| :--- | :--- | :--- |
| **Condicional `if / elif / else`** | `if opcion == "1": ... elif opcion == "8": ... else:` | Toma de decisiones en el menú y evaluación de reglas de negocio (aprobado/reprobado). |
| **Bucle `while`** | `while True:` | Mantiene en ejecución el menú principal y repite solicitudes de entrada hasta que sean válidas. |
| **Bucle `for`** | `for nota in listaNotas: suma += nota` | Itera de forma finita y controlada sobre listas de notas y estudiantes para acumular y mostrar datos. |
| **Funciones (`def`)** | `def calcularPromedio(listaNotas):` | Organiza el programa en bloques reutilizables, legibles y fáciles de probar. |
| **Listas (`[]`)** | `estudiante["notas"].append(nota)` | Colección ordenada y mutable para acumular dinámicamente las notas de cada estudiante. |
| **Diccionarios (`{}`)** | `{"nombre": nombre, "notas": []}` | Estructura clave-valor ideal para asociar atributos de una misma entidad académica. |

---

## 9. Conclusión Inicial del Proyecto
El diseño del **Sistema de Gestión de Estudiantes y Notas** satisface de manera integral todos los requerimientos pedagógicos de un curso de lógica de programación. 

Al estructurarse sobre funciones claras, validaciones de datos exhaustivas y colecciones nativas de Python, el proyecto garantiza legibilidad, facilidad de explicación en exposiciones orales o videos evaluativos, y una base sólida para demostrar habilidades en control de versiones con Git y GitHub.
