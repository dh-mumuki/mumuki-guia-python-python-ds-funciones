class TestFixtures(unittest.TestCase):
  def test_mismo_signo(self):
    self.assertEquals(cuadrado_de_suma(1, 2), 9, "Revisa la funcion, debes sumar primero y a ese resultado aplicar el cuadrado")
    
  def test_distinto_signo(self):
    self.assertEquals(cuadrado_de_suma(-10, 3), 49, "Revisa la funcion, cuando el signo es negativo, la suma se transforma en resta.")
  