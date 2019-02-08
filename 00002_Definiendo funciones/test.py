class TestFixtures(unittest.TestCase):
  
  def test_mitad_entero(self):
    self.assertEquals(mitad(4),2, 'La funcion no entrega el resultado correcto cuando el valor es un entero positivo')
  
  def test_mitad_negativo(self):
    self.assertEquals(mitad(-4), -2, 'La funcion no devuelve el resultado correcto cuando el numero es negativo')
  
  def test_mitad_negativo_float(self):
    self.assertAlmostEqual(mitad(-4.5), -2.25, 'La funcion no devuelve el valor esperado cuando el numero es de tipo float negativo')