nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)
edad = input("¿Cuantos años tienes? ")
edad = int(edad)
anyo_actual = input("¿En qué año estamos? ")
anyo_actual = int(anyo_actual)
anyo_nacimiento = anyo_actual - edad

print(nombre, "naciste en", anyo_nacimiento)
