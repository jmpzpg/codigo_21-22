import unittest
from metodo_estatico import Calificaciones

class TestClaseCalificaciones(unittest.TestCase):
    def test_existencia(self):
        c = Calificaciones()
        self.assertNotEqual(c,None)

    def test_constructor_x_defecto_nombre_cadvacia_notas_listavacia_calificacion_cadvacia(self):
        c = Calificaciones()
        self.assertEqual(c.alumno, '')
        self.assertEqual(c.notas, [])
        self.assertEqual(c.calificacion, '')

    def test_constructor_asigna_valor_propiedades(self):
        c = Calificaciones(['Raul', 9.2, 5, 4.5, 7, 9.1])
        self.assertEqual(c.alumno, 'Raul')
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

    def test_set_alumno_vacio_actualiza_nombre_y_notas(self):
        c = Calificaciones()
        c.set_alumno(['Pedro', 9.5])
        self.assertEqual(c.alumno, 'Pedro')
        self.assertEqual(c.notas, [9.5])
        self.assertEqual(c.calificacion, 'EXCELENTE') 

    def test_asigna_valores_alumno_vacio(self):
        c = Calificaciones()
        c.nombre = 'Paco' 
        self.assertEqual(c.nombre, 'Paco')


    def test_asigna_notas(self):
        c = Calificaciones()
        c.notas = [5,6,7,8,9,10]
        self.assertEqual(c.notas, [5,6,7,8,9,10])
        self.assertEqual(c.calificacion, 'NOTABLE') 

    def test_validar_notas_incorrectas(self):
        notas_a_validar = [11]
        self.assertEqual(Calificaciones.valida_notas(notas_a_validar), False)

    def test_validar_notas_incorrectas_cadena(self):
        notas_a_validar = [10, 'hola']
        self.assertEqual(Calificaciones.valida_notas(notas_a_validar), False)
    
    def test_validar_notas_incorrectas_lista_vacia(self):
        notas_a_validar = []
        self.assertEqual(Calificaciones.valida_notas(notas_a_validar), False)

    def test_validar_notas_correctas(self):
        notas_a_validar = [5.3]
        self.assertEqual(Calificaciones.valida_notas(notas_a_validar), True)