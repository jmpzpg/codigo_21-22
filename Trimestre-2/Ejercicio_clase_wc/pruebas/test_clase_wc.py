import unittest
from jmpp_wc import WC

class TestClaseWC(unittest.TestCase):
    def test_existencia(self):
        w = WC()
        self.assertIsNotNone(w)

    def test_pedir_num_lineas_dev_num_lineas(self):
        w = WC()
        resp = w.num_lineas
        self.assertEqual(resp, 0)

    def test_pedir_num_palabras_dev_num_palabras(self):
        w = WC()
        resp = w.num_palabras
        self.assertEqual(resp, 0)

    def test_pedir_num_ocurrencias_dev_num_ocurrencias(self):
        w = WC()
        resp = w.num_ocurrencias
        self.assertEqual(resp, {})

    