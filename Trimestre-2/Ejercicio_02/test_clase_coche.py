import unittest
from Ejer_02_clase_coche import Coche

class TestClaseCoche(unittest.TestCase):
    def test_clase_existe(self):
        c = Coche()
        self.assertNotEqual(c, None)

    def test_constructor_x_defecto_da_todas_las_propiedades_cadena_vacia(self):
        c = Coche()
        self.assertEqual(c.marca, '')
        self.assertEqual(c.modelo, '')
        self.assertEqual(c.color, '')
        self.assertEqual(c.num_puertas, '')
        self.assertEqual(c.matricula, '')
    
    def test_constructor_con_argumentos(self):
        c = Coche('Seat','León','rojo pasión','5','2022-DAM')
        self.assertEqual(c.marca, 'Seat')
        self.assertEqual(c.modelo, 'León')
        self.assertEqual(c.color, 'rojo pasión')
        self.assertEqual(c.num_puertas, '5')
        self.assertEqual(c.matricula, '2022-DAM')
    
    def test_marca_set_y_get_valor_propiedad(self):
        c = Coche()
        c.marca = 'Tesla'
        self.assertEqual(c.marca, 'Tesla')
    def test_modelo_set_y_get_valor_propiedad(self):
        c = Coche()
        c.modelo = 'Alhambra'
        self.assertEqual(c.modelo, 'Alhambra')
    def test_color_set_y_get_valor_propiedad(self):
        c = Coche()
        c.color = 'blanco mate'
        self.assertEqual(c.color, 'blanco mate')
    def test_num_puertas_set_y_get_valor_propiedad(self):
        c = Coche()
        c.num_puertas = 3
        self.assertEqual(c.num_puertas, '3')
    def test_matricula_set_y_get_valor_propiedad(self):
        c = Coche()
        c.matricula = '2044-BLR'
        self.assertEqual(c.matricula, '2044-BLR')
    
    def test_imprimir_caracteristicas_coche(self):
        c = Coche('Kia','Niro','azul cielo otoñal', 5, '1234-ABC')
        self.assertEqual(c.__str__(), '---------------------------------\nLas características del COCHE son: \n---------------------------------\n   Marca -------------> Kia\n   Modelo ------------> Niro\n   Color -------------> azul cielo otoñal\n   Número de puertas -> 5\n   Matrícula ---------> 1234-ABC\n. . . . . . . . . . . . . . . . . ')

