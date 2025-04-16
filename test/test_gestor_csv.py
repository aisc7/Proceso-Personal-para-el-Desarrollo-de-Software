import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from gestor_csv import GestorCSV
from estudiante import Estudiante

class TestGestorCSV(unittest.TestCase):
    def setUp(self):
        self.datos = [
            "1234567,Lulú López,1040,Cálculo",
            "9876534,Pepito Pérez,1040,Cálculo",
            "4567766,Calvin Clein,1050,Física I",
            "1234567,Lulú López,1060,Administración",
            "4567766,Calvin Clein,1070,Espíritu Empresarial"
        ]
        self.gestor = GestorCSV()

    def test_procesarDatos(self):
        estudiantes = self.gestor.procesarDatos(self.datos)
        self.assertEqual(estudiantes["1234567"].contarMaterias(), 2)
        self.assertEqual(estudiantes["9876534"].contarMaterias(), 1)
        self.assertEqual(estudiantes["4567766"].contarMaterias(), 2)

    def test_contarMaterias(self):
        est = Estudiante("123", "Ejemplo Estudiante")
        est.agregarMateria("1010")
        est.agregarMateria("2020")
        est.agregarMateria("1010")  # No debería contarla dos veces
        self.assertEqual(est.contarMaterias(), 2)

if __name__ == '__main__':
    unittest.main()
