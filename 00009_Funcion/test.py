class TestFixtures(unittest.TestCase):
  def mismo_signo(self):
    self.assertEquals(cuadrado_de_suma(1, 2), 9)
    
  def distinto_signo(self):
    self.assertEquals(cuadrado_de_suma(-10, 3), 49)
  