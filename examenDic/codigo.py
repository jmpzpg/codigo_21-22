def sumar(arg):
    total = 0
    for val in arg:
        total += val
    return total

# ------------------------------------

def test_si_no_arg_devuelve_cero():
     #   return 0
     
def test_si_lista_de_int_o_float_devuelve_suma(self):
        resp = codigo.sumar([1,3,5.5])
        self.assertEqual(resp,9.5)
       
def test_si_cadenas_devuelve_cero():
    return 0
def test_si_num_complejos_devuelve_cero():
    return 0
def test_si_obj_no_numericos_devuelve_cero():
    return 0

lista_num = [2,3.5,4]
print(f'La suma de la lista de números es = {sumar(lista_num)}')