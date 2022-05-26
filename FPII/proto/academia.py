class Alumno():
    def __init__(self, n, ap, email):
        self.nombre = n
        self.apellidos = ap
        self.correo_e = email

        self.asignaturas = []
        self.movil = ''
        self._horas_mensuales = 0


    def alta_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise Exception("{} debe ser un objeto de tipo Asignatura".
                            format(asignatura))

        if asignatura in self.asignaturas:
            return
        self.asignaturas.append(asignatura)

    def __str__(self):
        return "Alumno: {} {} - {}".format(self.nombre, self.apellidos, self.correo_e)
    

class Asignatura():
    def __init__(self, nombre, precio_h):
        self.nombre = nombre
        self.precio = precio_h

    def __str__(self):
        return "{} - 1 hora semanal ({} € al mes) ".format(self.nombre, self.precio)

    def __repr__(self):
        return self.__str__()


class Profesor():
    def __init__(self, n, ap, email, sueldo_base=200):
        self.nombre = n
        self.apellidos = ap
        self.correo_e = email

        self.asignaturas = []
        self.movil = ''
        self._horas_mensuales = 0

        self.sueldo_base = sueldo_base

    def alta_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise Exception("{} debe ser un objeto de tipo Asignatura".
                        format(asignatura))

        if asignatura in self.asignaturas:
            return
        self.asignaturas.append(asignatura)

    def __str__(self):
        return "Profesor: {} {} - {}".format(self.nombre, self.apellidos, self.correo_e)

    def sueldo(self):
        return self.sueldo_base + len(self.asignaturas) * 300
