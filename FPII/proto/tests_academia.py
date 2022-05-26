from academia import Alumno, Asignatura, Profesor

'''
Prueba para crear un alumno
    - Pedro Jimenez Guerra, pjg@gmail.com
'''

pedro = Alumno("Pedro", "Jimenez Guerra", "pjg@gmail.com")
print(pedro)
print(pedro.movil)
print(pedro.asignaturas)

'''
Prueba para crear dos asignaturas
    - INGLES: 20€
    - CHINO: 30€
'''

ingles = Asignatura("Ingles", 20.0)
chino = Asignatura("Chino", 30.0)

print(ingles)
print(chino)


'''
Prueba para asociar chino a pedro
'''
pedro.alta_asignatura(chino)
pedro.alta_asignatura(ingles)
pedro.alta_asignatura(chino)

print("Asignaturas de", pedro)
print(pedro.asignaturas)

'''
Prueba de creación de Segismundo, profesor de inglés
'''

segis = Profesor("Segismundo", "Bejarano Revilla", "sbr@email.com")
segis.alta_asignatura(ingles)

print(segis)
print("Asignaturas de", segis)
print(segis.asignaturas)

print("Sueldo:", segis.sueldo(), "€/mes")

segis.horas_mensuales = 6
pedro.horas_mensuales = 4

print(segis.horas_mensuales, pedro.horas_mensuales)