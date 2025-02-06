dividendo = int(input("Introduce un dividendo: "))
divisor = int(input("Introduce un divisor: "))

if (divisor == 0):
    print("Error: no se puede dividir por cero.")
    exit()

cociente = dividendo // divisor
print(f"El resultado es ",divisor)
