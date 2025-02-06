# Ejercicio 8: Clases y objetos
# Crea una clase llamada `Coche` que tenga:
# - Atributos: marca, modelo y año.
# - Un método `mostrar_info()` que imprima la información del coche. Luego crea dos objetos de la clase `Coche` y muestra su información.


class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

# Creando objetos de la clase Coche
coche1 = Coche("Renault", "Clio", 2010)
coche2 = Coche("Opel", "Astra", 2022)

equipo = [coche1, coche2]

# Mostrando información de los coches
for coche in equipo:
    coche.mostrar_info()
    print("--------------------")
