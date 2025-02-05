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
    
def asignaturas_notas(alumnos):
    alumno = input("Introduce el nombre del alumno: ")
    
    if (alumno) not in alumnos:
        print("El alumno no existe.")
        return
    
    for _ in range(3):
        nombreAsignatura = input("Introduce el nombre de la asignatura: ")
        notas = []
        for trimestre in range(1,4):
            nota = float(input(f"Introduce la nota del trimestre:{trimestre} "))
        notas.append(nota)
    
    notaAsignatura = input(float("Nota: "))
    
    