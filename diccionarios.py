diccionario = {
    "persona01": {
        "nombre": "Juan",
        "edad": 24,
    },
    "persona02": {
        "nombre": "Pedro",
        "edad": 27,
    },
    "persona03": {
        "nombre": "Maria",
        "edad": 17,
    }
}

nombre = input("Introduce un nombre: ")

encontrado = False

for persona in diccionario.values():
    if persona["nombre"] == nombre:  #
        print(f"Se ha encontrado {nombre}: Edad: {persona['edad']}")
        encontrado = True
        break  # Si lo encontramos, no es necesario seguir buscando

if not encontrado:
    print(f"No se encontró ninguna persona llamada {nombre}.")