class TestFixtures(unittest.TestCase):
  def Mismo_signo_al_cuadrado(self):
    self.assertEquals(cuadrado_de_suma(1, 2), 9, "Revisa la función, algo no esta bien")
    
  def Distinto_signo_al_cuadrado(self):
    self.assertEquals(cuadrado_de_suma(-10, 3),49, "Revisa la función, algo no esta bien")
  