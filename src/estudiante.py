# Tomamos en base al modelo A
class Estudiante:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.materias = set()

    def agregarMateria(self, codigo):
        self.materias.add(codigo)

    def contarMaterias(self):
        return len(self.materias)
