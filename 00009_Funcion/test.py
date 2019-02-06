class TestFixtures(unittest.TestCase):
  def test_mismo_signo(self):
    self.assertEquals(cuadrado_de_suma(1, 2), 9)
    
  def test_distinto_signo(self):
    self.assertEquals(cuadrado_de_suma(-10, 3), 49)
  