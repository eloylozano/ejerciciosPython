a = int(input("Introduce el valor de la variable A: "))
b = int(input("Introduce el valor de la variable B: "))

aux = a
a = b
b = aux
print(aux)
print(a)
print(b)
