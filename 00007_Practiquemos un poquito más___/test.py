class TestFixtures(unittest.TestCase):
  def test_dos(self):
    self.assertEquals(producto(2, 2),4, 'El producto entre dos numeros positivos es incorrecto')
  
  def test_negativo(self):
    self.assertEquals(producto(-4, 4),-16, 'El producto entre un numero negativo y otro positivo es incorrecto')