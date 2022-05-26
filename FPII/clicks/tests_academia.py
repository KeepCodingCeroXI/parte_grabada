from academia import Alumno, Asignatura, Profesor

roberto = Alumno('Roberto', 'Rodríguez')
susana = Alumno('Susana', 'Martín')

print(roberto.nombre, roberto.apellidos, roberto) # Roberto Rodríguez
print(susana.nombre, susana.apellidos, susana) # Susana Martín

print(roberto.correo_e, roberto.movil) # 

ingles = Asignatura("Inglés", 'A2')
ingles.precio_h = 7.5
aleman = Asignatura("Alemán", 'A2')
aleman.precio_h = 8

chino = Asignatura("Chino Cantonés", 'A1')
chino.precio_h = 10



print(ingles) # Asignatura: Inglés - A2 - (30.00 €/mes)

roberto.alta_asignatura(ingles)
roberto.alta_asignatura(chino)

print(roberto.asignaturas) # [Asignatura: Inglés - A2 - (30.00 €/mes), Asignatura: Chino...]
print(susana.asignaturas) # 

donJose = Profesor("José", "Martin Fusta", '0W', "jf@email.com")
print(donJose) #Profesor: 0W - José Martin Fusta - jf@email.com

print(donJose.sueldo()) #200

donJose.alta_asignatura(ingles)

print(donJose.asignaturas) # [Asignatura: Inglés - A2 - (30.00 €/mes)]
print(donJose.sueldo()) #500
