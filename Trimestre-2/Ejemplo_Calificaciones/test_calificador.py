import unittest
from metodo_estatico import Calificaciones

class TestClaseCalificaciones(unittest.TestCase):
    def test_existencia(self):
        c = Calificaciones()
        self.assertNotEqual(c,None)

    def test_constructor_x_defecto_nombre_cadvacia_notas_listavacia_calificacion_cadvacia(self):
        c = Calificaciones()
        self.assertEqual(c.nombre, '')
        self.assertEqual(c.notas, [])
        self.assertEqual(c.calificacion, '')

    def test_constructor_asigna_valor_propiedades(self):
        c = Calificaciones(['Raul', 9.2, 5, 4.5, 7, 9.1])
        self.assertEqual(c.nombre, 'Raul')
        self.assertEqual(c.notas, [9.2, 5, 4.5, 7, 9.1])

    def test_metodo_str_dev_alumno_calificacion(self):
        c = Calificaciones(['Raul', 9.2, 5, 4.5, 7, 9.1])
        cadena = c.__str__()
        self.assertEqual(cadena, 'Alumno: Raul tiene la calificación: NOTABLE')

    def test_calcula_calificacion_vacio_dev_None(self):
        c = Calificaciones()
        self.assertEqual(c.calcula_calificacion(), None)   

    def test_calcula_calificacion_no_vacio_dev_calificacion(self):
        c = Calificaciones(['Raul', 9.2, 5, 4.5, 7, 9.1])
        self.assertEqual(c.calcula_calificacion(), 'NOTABLE') 
        self.assertEqual(c.calificacion, 'NOTABLE')