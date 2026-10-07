"""
=============================================================================
SISTEMA DE GESTIÓN DE ESTUDIANTES Y NOTAS
Proyecto Académico de Lógica de Programación
Lenguaje: Python (Consola / Terminal)
Estilo de Nomenclatura: camelCase
=============================================================================
"""

# Lista principal para almacenar los estudiantes.
# Cada estudiante es un diccionario: {"nombre": str, "notas": [float, ...]}
estudiantes = []


def mostrarMenu():
    """Muestra en pantalla el menú principal con las opciones disponibles."""
    print("\n" + "=" * 50)
    print("      SISTEMA DE GESTIÓN DE ESTUDIANTES Y NOTAS")
    print("=" * 50)
    print("1. Registrar estudiante")
    print("2. Ingresar notas de un estudiante")
    print("3. Mostrar todos los estudiantes registrados")
    print("4. Buscar un estudiante por nombre")
    print("5. Calcular y mostrar promedio de un estudiante")
    print("6. Mostrar si el estudiante está aprobado o reprobado")
    print("7. Mostrar resumen general del curso")
    print("8. Salir del programa")
    print("=" * 50)


def buscarEstudiante(nombre):
    """
    Busca un estudiante en la lista por su nombre sin distinguir mayúsculas/minúsculas.
    Retorna el diccionario del estudiante si existe, o None si no se encuentra.
    """
    nombreLimpio = nombre.strip().lower()
    for estudiante in estudiantes:
        if estudiante["nombre"].strip().lower() == nombreLimpio:
            return estudiante
    return None


def registrarEstudiante():
    """
    Registra un nuevo estudiante en el sistema validando:
    - Que el nombre no esté vacío.
    - Que no exista ya un estudiante con el mismo nombre.
    """
    print("\n--- REGISTRAR ESTUDIANTE ---")
    while True:
        nombre = input("Ingrese el nombre completo del estudiante (o 'c' para cancelar): ").strip()

        # Permitir cancelar la operación si el usuario lo desea
        if nombre.lower() == 'c':
            print("Operación cancelada. Regresando al menú principal.")
            return

        # Validación 1: El nombre no puede ser una cadena vacía
        if not nombre:
            print("Error: El nombre no puede estar vacío. Por favor, intente nuevamente.")
            continue

        # Validación 2: No permitir nombres duplicados
        if buscarEstudiante(nombre) is not None:
            print(f"Error: Ya existe un estudiante registrado con el nombre '{nombre}'.")
            continue

        # Estructura del nuevo estudiante: diccionario con nombre y lista de notas vacía
        nuevoEstudiante = {
            "nombre": nombre,
            "notas": []
        }
        estudiantes.append(nuevoEstudiante)
        print(f"Éxito: El estudiante '{nombre}' fue registrado correctamente.")
        break


def ingresarNotas():
    """
    Permite registrar calificaciones (0.0 a 10.0) para un estudiante existente.
    Valida entradas numéricas y que los valores se encuentren en el rango permitido.
    """
    print("\n--- INGRESAR NOTAS ---")
    if not estudiantes:
        print("Aviso: No hay estudiantes registrados en el sistema.")
        return

    nombre = input("Ingrese el nombre del estudiante al que desea agregar notas: ").strip()
    estudiante = buscarEstudiante(nombre)

    if estudiante is None:
        print(f"Error: No se encontró al estudiante '{nombre}'.")
        return

    print(f"Estudiante seleccionado: {estudiante['nombre']}")
    if estudiante["notas"]:
        notasActuales = ", ".join(f"{n:.1f}" for n in estudiante["notas"])
        print(f"Notas registradas actualmente: [{notasActuales}]")
    else:
        print("Notas registradas actualmente: [Sin notas]")

    # Validar cuántas notas se desean registrar en esta sesión
    while True:
        entradaCantidad = input("¿Cuántas notas desea ingresar? (Número entero positivo): ").strip()
        if entradaCantidad.isdigit() and int(entradaCantidad) > 0:
            cantidad = int(entradaCantidad)
            break
        else:
            print("Error: Por favor, ingrese un número entero mayor a cero.")

    # Bucle para solicitar y validar cada nota en la escala de 0.0 a 10.0
    for i in range(1, cantidad + 1):
        while True:
            entradaNota = input(f"Ingrese la nota #{i} (entre 0.0 y 10.0): ").strip()
            # Permitir ingreso con coma decimal (ej. 8,5 -> 8.5)
            entradaNota = entradaNota.replace(',', '.')
            try:
                nota = float(entradaNota)
                if 0.0 <= nota <= 10.0:
                    estudiante["notas"].append(nota)
                    print(f"-> Nota {nota:.1f} registrada correctamente.")
                    break
                else:
                    print("Error: La calificación debe estar entre 0.0 y 10.0.")
            except ValueError:
                print("Error: Valor inválido. Debe ingresar un número (ejemplo: 8.5 o 10).")

    notasFinales = ", ".join(f"{n:.1f}" for n in estudiante["notas"])
    print(f"\nLista de notas actualizada de {estudiante['nombre']}: [{notasFinales}]")


def calcularPromedio(listaNotas):
    """
    Calcula el promedio aritmético de una lista de notas utilizando un bucle for.
    Retorna 0.0 si la lista está vacía.
    """
    if not listaNotas:
        return 0.0

    suma = 0.0
    for nota in listaNotas:
        suma += nota

    promedio = suma / len(listaNotas)
    return promedio


def determinarEstado(promedio):
    """
    Determina si un estudiante aprueba o reprueba según la regla de negocio:
    - Aprobado: promedio >= 7.0
    - Reprobado: promedio < 7.0
    """
    if promedio >= 7.0:
        return "APROBADO"
    else:
        return "REPROBADO"


def mostrarEstudiantes():
    """Muestra un listado general de todos los estudiantes registrados con sus notas y promedio."""
    print("\n--- LISTA GENERAL DE ESTUDIANTES REGISTRADOS ---")
    if not estudiantes:
        print("Aviso: Actualmente no hay estudiantes registrados.")
        return

    print("-" * 65)
    print(f"{'#':<4} {'Nombre':<25} {'Notas':<20} {'Promedio':<10}")
    print("-" * 65)

    for indice, est in enumerate(estudiantes, start=1):
        if est["notas"]:
            notasStr = ", ".join(f"{n:.1f}" for n in est["notas"])
            prom = calcularPromedio(est["notas"])
            promStr = f"{prom:.2f}"
        else:
            notasStr = "Sin notas"
            promStr = "N/A"

        print(f"{indice:<4} {est['nombre']:<25} {notasStr:<20} {promStr:<10}")
    print("-" * 65)


def buscarEstudianteInteractivo():
    """Permite buscar un estudiante por nombre y ver todo su detalle académico."""
    print("\n--- BUSCAR ESTUDIANTE POR NOMBRE ---")
    if not estudiantes:
        print("Aviso: No hay estudiantes registrados en el sistema.")
        return

    nombre = input("Ingrese el nombre del estudiante a buscar: ").strip()
    estudiante = buscarEstudiante(nombre)

    if estudiante is None:
        print(f"Resultado: No se encontró ningún estudiante con el nombre '{nombre}'.")
    else:
        print("\n" + "-" * 35)
        print("      INFORMACIÓN DEL ESTUDIANTE")
        print("-" * 35)
        print(f"Nombre    : {estudiante['nombre']}")
        if estudiante["notas"]:
            notasStr = ", ".join(f"{n:.1f}" for n in estudiante["notas"])
            promedio = calcularPromedio(estudiante["notas"])
            estado = determinarEstado(promedio)
            print(f"Notas     : [{notasStr}]")
            print(f"Promedio  : {promedio:.2f}")
            print(f"Estado    : {estado}")
        else:
            print("Notas     : Sin notas registradas")
            print("Promedio  : N/A")
            print("Estado    : Pendiente de calificaciones")
        print("-" * 35)


def mostrarPromedioIndividual():
    """Consulta y muestra el promedio de un estudiante específico."""
    print("\n--- CALCULAR PROMEDIO DE UN ESTUDIANTE ---")
    if not estudiantes:
        print("Aviso: No hay estudiantes registrados.")
        return

    nombre = input("Ingrese el nombre del estudiante: ").strip()
    estudiante = buscarEstudiante(nombre)

    if estudiante is None:
        print(f"Error: El estudiante '{nombre}' no está registrado.")
        return

    if not estudiante["notas"]:
        print(f"Aviso: El estudiante '{estudiante['nombre']}' no tiene notas registradas aún.")
        return

    promedio = calcularPromedio(estudiante["notas"])
    notasStr = ", ".join(f"{n:.1f}" for n in estudiante["notas"])
    print(f"\nEstudiante : {estudiante['nombre']}")
    print(f"Notas      : [{notasStr}]")
    print(f"Promedio   : {promedio:.2f} / 10.0")


def mostrarEstadoIndividual():
    """Determina y muestra en consola si un estudiante aprueba o reprueba."""
    print("\n--- ESTADO DE APROBACIÓN DE UN ESTUDIANTE ---")
    if not estudiantes:
        print("Aviso: No hay estudiantes registrados.")
        return

    nombre = input("Ingrese el nombre del estudiante: ").strip()
    estudiante = buscarEstudiante(nombre)

    if estudiante is None:
        print(f"Error: El estudiante '{nombre}' no está registrado.")
        return

    if not estudiante["notas"]:
        print(f"Aviso: El estudiante '{estudiante['nombre']}' no posee notas para determinar su estado.")
        return

    promedio = calcularPromedio(estudiante["notas"])
    estado = determinarEstado(promedio)

    print(f"\nEstudiante : {estudiante['nombre']}")
    print(f"Promedio   : {promedio:.2f}")
    if estado == "APROBADO":
        print(f"Resultado  : ¡{estado}! (El promedio es mayor o igual a 7.0)")
    else:
        print(f"Resultado  : {estado} (El promedio es menor a 7.0)")


def mostrarResumenGeneral():
    """
    Genera un informe con estadísticas generales del curso:
    - Cantidad total de estudiantes.
    - Estudiantes evaluados y pendientes.
    - Cantidad de aprobados y reprobados.
    - Promedio general del curso y mejores/peores rendimientos.
    """
    print("\n--- RESUMEN GENERAL DEL CURSO ---")
    totalEstudiantes = len(estudiantes)
    if totalEstudiantes == 0:
        print("Aviso: No hay estudiantes registrados en el sistema.")
        return

    aprobados = 0
    reprobados = 0
    sinNotas = 0
    sumaPromedios = 0.0
    evaluados = 0

    mejorPromedio = -1.0
    mejorEstudiante = ""
    peorPromedio = 11.0
    peorEstudiante = ""

    # Bucle for para analizar las notas de cada estudiante
    for est in estudiantes:
        if not est["notas"]:
            sinNotas += 1
        else:
            prom = calcularPromedio(est["notas"])
            sumaPromedios += prom
            evaluados += 1

            # Estructura condicional if / else para clasificar aprobado / reprobado
            if prom >= 7.0:
                aprobados += 1
            else:
                reprobados += 1

            # Determinar el promedio más alto y más bajo
            if prom > mejorPromedio:
                mejorPromedio = prom
                mejorEstudiante = est["nombre"]

            if prom < peorPromedio:
                peorPromedio = prom
                peorEstudiante = est["nombre"]

    print(f"Total de estudiantes registrados : {totalEstudiantes}")
    print(f"Estudiantes evaluados con notas  : {evaluados}")
    print(f"Estudiantes pendientes sin notas : {sinNotas}")
    print(f"Total de APROBADOS (>= 7.0)       : {aprobados}")
    print(f"Total de REPROBADOS (< 7.0)       : {reprobados}")

    # Cálculo y presentación de estadísticas grupales si hay estudiantes evaluados
    if evaluados > 0:
        promedioCurso = sumaPromedios / evaluados
        print(f"Promedio general del grupo       : {promedioCurso:.2f} / 10.0")
        print(f"Mejor rendimiento académico      : {mejorEstudiante} (Promedio: {mejorPromedio:.2f})")
        print(f"Menor rendimiento académico      : {peorEstudiante} (Promedio: {peorPromedio:.2f})")
    else:
        print("Aviso: Ningún estudiante cuenta con notas aún para calcular promedios grupales.")


def main():
    """Función principal del programa. Controla el menú cíclico mediante un bucle while."""
    print("\n¡Bienvenido al Sistema de Gestión de Estudiantes y Notas!")

    # Bucle repetitivo principal para mantener activo el menú hasta que el usuario elija salir
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción (1-8): ").strip()

        # Estructura condicional if / elif / else para despachar cada opción
        if opcion == "1":
            registrarEstudiante()
        elif opcion == "2":
            ingresarNotas()
        elif opcion == "3":
            mostrarEstudiantes()
        elif opcion == "4":
            buscarEstudianteInteractivo()
        elif opcion == "5":
            mostrarPromedioIndividual()
        elif opcion == "6":
            mostrarEstadoIndividual()
        elif opcion == "7":
            mostrarResumenGeneral()
        elif opcion == "8":
            print("\n¡Gracias por utilizar el sistema! El programa ha finalizado exitosamente.\n")
            break  # Rompe el bucle while y finaliza la ejecución
        else:
            print(f"\nError: La opción '{opcion}' no es válida. Ingrese un número entre 1 y 8.")


# Punto de entrada para ejecutar el archivo directamente
if __name__ == "__main__":
    main()
