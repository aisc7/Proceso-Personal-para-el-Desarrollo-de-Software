from estudiante import Estudiante

# Tomamos en base al modelo A
class GestorCSV:
    def leerArchivo(self, ruta):
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.readlines()

    def procesarDatos(self, datos):
        estudiantes = {}
        for linea in datos:
            partes = linea.strip().split(',')
            if len(partes) < 4:
                continue

            cedula, nombre, cod_materia, _ = partes

            if cedula not in estudiantes:
                estudiantes[cedula] = Estudiante(cedula, nombre)

            estudiantes[cedula].agregarMateria(cod_materia)

        return estudiantes

    def mostrarResumen(self, estudiantes):
        for est in estudiantes.values():
            print(f"{est.nombre}: {est.contarMaterias()} materias")


# Ejecución principal
if __name__ == "__main__":
    gestor = GestorCSV()
    ruta = input("Ingrese la ruta del archivo CSV: ")
    try:
        datos = gestor.leerArchivo(ruta)
        estudiantes = gestor.procesarDatos(datos)
        gestor.mostrarResumen(estudiantes)
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
