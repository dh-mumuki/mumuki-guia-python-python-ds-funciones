class TestFixtures(unittest.TestCase):
  
  def test_mitad_entero(self):
    self.assertEquals(mitad(4),2)
  
  def test_mitad_negativo(self):
    self.assertEquals(mitad(-4), -2)
  
  def test_mitad_negativo_float(self):
    self.assertAlmostEqual(mitad(-4.5), -2.25)