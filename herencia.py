### Ejercicio 9: Herencia
# Crea una clase base `Animal` con un método `hacer_sonido()`. Luego, crea dos clases hijas `Perro` y `Gato` que sobrescriban el método para mostrar sonidos diferentes. Crea instancias de ambas clases y llama al método `hacer_sonido()`.


class Animal:
    def hacer_sonido(self):

        print("El animal hace sonido.")


class Perro(Animal):
    def hacer_sonido(self):

        print("El perro ladrará.")


class Gato(Animal):
    def hacer_sonido(self):

        print("El gato maulla.")
        
# Crear instancias
animal = Animal()
perro = Perro()
gato = Gato()

# Llamar a los métodos
animal.hacer_sonido()  # "El animal hace un sonido."
perro.hacer_sonido()   # "El perro ladra."
gato.hacer_sonido() 