def menu():
    print("\nMenu:")
    print("1. Alta de alumno")
    print("2. Alta asignatura y notas")
    print("3. Mostrar nota media global de cada alumno")
    print("4. Mostrar notas medias de cada asignatura")
    print("5. Mostrar notas de un alumno")
    print("6. Salir")


def alta_alumno(alumnos):
    nombre = input("Introduce el nombre del alumno: ")
    edad = int(input("Introduce la edad del alumno: "))
    telefono = input("Introduce el teléfono del alumno: ")
    alumnos[nombre] = {'edad': edad, 'telefono': telefono, 'asignaturas': {}}
    print(f"Alumno {nombre} añadido correctamente.")


def alta_asignaturas(alumnos):
    nombre = input("Introduce el nombre del alumno: ")
    if nombre not in alumnos:
        print("El alumno no existe. Debes darlo de alta primero.")
        return

    for _ in range(3):
        asignatura = input("Introduce el nombre de la asignatura: ")
        notas = []
        for trimestre in range(1, 4):
            nota = float(input(f"Introduce la nota del trimestre {trimestre}: "))
            notas.append(nota)
        alumnos[nombre]['asignaturas'][asignatura] = notas
    print(f"Asignaturas y notas añadidas para {nombre}.")


def mostrar_media_global(alumnos):
    medias = []
    for nombre, datos in alumnos.items():
        total_notas = 0
        contador = 0
        for notas in datos['asignaturas'].values():
            total_notas += sum(notas)
            contador += len(notas)
        media_global = total_notas / contador if contador != 0 else 0
        medias.append((nombre, media_global))
    print("\nNota media global de cada alumno:")
    for nombre, media in medias:
        print(f"{nombre}: {media:.2f}")


def mostrar_media_asignaturas(alumnos):
    asignaturas_notas = {}
    for datos in alumnos.values():
        for asignatura, notas in datos['asignaturas'].items():
            if asignatura not in asignaturas_notas:
                asignaturas_notas[asignatura] = []
            asignaturas_notas[asignatura].extend(notas)

    medias_asignaturas = set()
    print("\nNota media de cada asignatura:")
    for asignatura, notas in asignaturas_notas.items():
        media = sum(notas) / len(notas)
        medias_asignaturas.add(media)
        print(f"{asignatura}: {media:.2f}")


def mostrar_notas_alumno(alumnos):
    nombre = input("Introduce el nombre del alumno: ")
    if nombre not in alumnos:
        print("El alumno no existe.")
        return

    datos = alumnos[nombre]
    total_notas = 0
    contador = 0
    print(f"\nNotas de {nombre}:")
    for asignatura, notas in datos['asignaturas'].items():
        media_asignatura = sum(notas) / len(notas)
        total_notas += sum(notas)
        contador += len(notas)
        print(f"{asignatura}: {media_asignatura:.2f}")
    media_global = total_notas / contador if contador != 0 else 0
    print(f"Nota media global: {media_global:.2f}")


# Programa principal
alumnos = {}

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        alta_alumno(alumnos)
    elif opcion == '2':
        alta_asignaturas(alumnos)
    elif opcion == '3':
        mostrar_media_global(alumnos)
    elif opcion == '4':
        mostrar_media_asignaturas(alumnos)
    elif opcion == '5':
        mostrar_notas_alumno(alumnos)
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor selecciona una opción del 1 al 6.")
