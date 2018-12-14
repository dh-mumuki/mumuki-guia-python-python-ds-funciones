class TestFixtures(unittest.TestCase):
  def test_listas_1(self):
    self.assertEquals(tipo_de_dato(5), False)
    
  def test_listas_2(self):
    self.assertEquals(tipo_de_dato(5.0), True)
    
  def test_listas_3(self):
    self.assertEquals(tipo_de_dato("cinco"), True)
    
  def test_listas_4(self):
    self.assertEquals(tipo_de_dato(True), False)