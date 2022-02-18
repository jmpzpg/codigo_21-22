import unittest
from orden_por_insercion import ordena_lista

class TestOrdenInsercion(unittest.TestCase):
    def test_ordena_lista_vacia_dev_lista_vacia(self):
        lista = []
        resp = ordena_lista(lista)
        self.assertEqual(resp, [])
    
    def test_ordena_lista_dev_lista_ordenada(self):
        lista = [5,4,3,2,1]
        resp = ordena_lista(lista)
        self.assertEqual(resp, [1,2,3,4,5]) 

    def test_ordena_lista_ejemplo_dev_lista_ordenada(self):
        lista = [4,3,2,10,12,1,5,6]
        resp = ordena_lista(lista)
        self.assertEqual(resp, [1,2,3,4,5,6,10,12]) 