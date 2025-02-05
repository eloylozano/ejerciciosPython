horapartida = int(input("Hora de salida: "))
minpartida = int(input("Minutos de salida: "))
segpartida = int(input("Segundos de salida: "))
segviaje = int(input("Tiempo que has tardado en segundos: "))
# Convierto la hora de salida a segundos
seginicial = horapartida * 3600 + minpartida * 60 + segpartida

# Sumo los segundos de viaje al tiempo inicial

segfinal = seginicial + segviaje

horallegada = segfinal // 3600
minllegada = (segfinal % 3600) // 60
segllegada = (segfinal % 3600) % 60

print("Hora de llegada")
print(horallegada, ":", minllegada, ":" ,segllegada )