from _typeshed import Self
import unittest
import codigo

class TestCodigo(unittest.TestCase):

    #def caracteres_no_numericos_devuelve_error(self):
    #    respuesta = calculadora.sumar('a,b')
    #    self.assertEqual(respuesta, 'Error: Carácter NO numérico')

    #def test_uno(self):
     #   pass
    #def test_si_no_arg_devuelve_cero():
     #   return 0
     
    def test_si_lista_de_int_o_float_devuelve_suma(self):
        resp = codigo.sumar([1,3,5.5])
        self.assertEqual(resp,9.5)
       
    #def test_si_cadenas_devuelve_cero():
    #    return 0
    #def test_si_num_complejos_devuelve_cero():
    #    return 0
    #def test_si_obj_no_numericos_devuelve_cero():
    #    return 0
    