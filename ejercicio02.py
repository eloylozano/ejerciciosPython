parcial1 = float(input("Dime la nota del parcial 1:"))
parcial2 = float(input("Dime la nota del parcial 2:"))
parcial3 = float(input("Dime la nota del parcial 3:"))
examen = float(input("Dime la nota del examen: "))
trabajo = float(input("Dime la nota del trabajo: "))

nota = ((parcial1 +parcial2 + parcial3) /3) * 0.55 + 0.3 * examen + 0.15 * trabajo

print("La nota final es:", round(nota, 2))